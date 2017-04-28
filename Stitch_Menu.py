#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
import StringIO
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print colored('DISCLAIMER','red','on_white')

print """
Stitch is relatively easy to understand and use after installation.
And it's far better documented than either Metasploit or Pupy.
IMO it's 'targeted-for-dummies'

If you have any questions please refer to 'Crash Course of Stitch': https://github.com/nathanlopez/Stitch/wiki/Crash-Course
"""
def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#INSTALL, Run the Stitch Installer',
        '#1. Run Stitch'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("ENTER A OPTION: "))

    if opt_Choice == "0":
        os.system('python /root/ArmsCommander/ArmsCommander.py')
    elif opt_Choice == "INSTALL":
        os.system('python /root/ArmsCommander/remoteexploits/stitchInstaller.py')
    elif opt_Choice == "1":
        os.system('python /root/Stitch/main.py')
    else:
        print '[-] You have entered a invalid option or type "INSTALL" + [Enter] to install Stitch'
        main()
    return
main()

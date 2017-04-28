import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

os.system('cat /root/ArmsCommander/banners/banner_DPMB.txt')
print colored("""Don't Patch Me Bro! The easy-mode inject.bin generator for the USB Rubber Ducky (from Hak5 Shop), \nthe Rubber Ducky is proprietary hardware sold to facilitate quick-and-easy BadUSB attacks
""",'red','on_white'
)
class parameters_Run_DuckYourself(object):
    def __init__(self, DuckEncoder_Location, DuckyScript_Location, SDCard_Location):
        self.DuckEncoder_Location = DuckEncoder_Location
        self.DuckyScript_Location = DuckyScript_Location
        self.SDCard_Location = SDCard_Location

    @classmethod
    def from_input(cls):
        return cls(
            '/root/ArmsCommander/remoteexploits/duckencode.jar',
            str(raw_input("Enter the location of your text file in DuckyScript: ")),
            str(raw_input("Enter the location of your SDCard: "))
        )

def run_DuckYourself():
    user_Input = parameters_Run_DuckYourself.from_input()

    cmd_String_Compile = "java -jar {0} -i {1} -o {2}/inject.bin".format(
        user_Input.DuckEncoder_Location,
        user_Input.DuckyScript_Location,
        user_Input.SDCard_Location
    )

    cmd_String_Eject = "eject %s" % user_Input.SDCard_Location
    print colored(cmd_String_Compile,'red','on_white')
    os.system(cmd_String_Compile)
    print colored(cmd_String_Eject,'red','on_white')
    os.system(cmd_String_Eject)
    print colored('Payload Generated and Entered into SDCard, insert it into RubberDucky, happy hacking!','red','on_white')
    return

def main():
    opt_List = [
        '\n\t#0. Return to the main menu',
        '#1. Convert your custom DuckyScript into a inject.bin file that will autorun on victim machines'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        run_DuckYourself()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
main()

import platform
import sys
import sched
import time
import keyboard
import ctypes
import os
import subprocess
import PySimpleGUI as sg
import threading
import json
oss = platform.system()
import pathlib
file = pathlib.Path("setup.txt")
import ctypes
import webbrowser
import signal
import re


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if oss == "Windows":
       if sys.argv[1] == "-setup":
         if not file.exists():
           if is_admin():
                print("If You Want To Donate! Go To https://www.paypal.me/soldeveloperm")
                os.system("netsh advfirewall firewall add rule name=\"SHORTCUT 80\" dir=in action=allow protocol=TCP localport=80")

                E = open("setup.txt", "w+")
                E.write("" + oss)
                E.close()
                sys.exit()
           else:

              ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
         else:
            print("You Already Setuped it")
       elif sys.argv[1] == "-run":

           # sg.Window().read()
           layout = [[sg.Text('Please Enter The IP that the Server will be running on')],
    [sg.Text('IP Address:', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()],[sg.Text('If You Want To Donate! Go To https://www.paypal.me/soldeveloperm')]]
           window = sg.Window(title="RPCC", layout=layout, margins=(100, 50))

           
           while True:
               event, values = window.read()
               

               if event == "Cancel" or event == sg.WIN_CLOSED:
                   window.close()
                   exit()
                   break
               elif event == "Submit":
                     window.close()
                     layouts = [[sg.Text("Server is running")], [sg.Button("Exit")]]
                     windowd = sg.Window("RPCC", layouts)
                     if __name__ == '__main__':
                        t = "php -S " + values[0] + ":80"
                        proc = subprocess.Popen(t, shell=False)
                        run = open("run.key", "r+")
                        run.truncate(0)
                        run.write("R")
                        run.close()
                        evente = windowd.read()
                        windowd.close()
                        if evente == "Exit" or evente == sg.WIN_CLOSED:
                             run = open("run.key", "r+")
                             text = run.read()
                             run.seek(0)
                             text = text.replace("R", "N")
                             run.write(text)
                             run.truncate()
                             run.close()
                             sys.exit()
                             break
       elif sys.argv[1] == "-load":
           with open('load.key', 'rt') as load:
               for line in load:
                   key = json.loads(line)
           run = open("run.key", "r")
           if run.readline() == "R":
               WTO = sys.argv[2]
               CV = key
               if WTO in CV:
                   Run = CV[str(WTO)]
                   subprocess.call([Run])
                   print("Done! " + WTO + " Is Running!")
           else:
               print("The Server Isnt Running?")




elif oss == "Darwin":
         print("Sorry " + oss +" Isnt Supported")
elif oss == "Linux":
         print("Sorry " + oss +" Isnt Supported")

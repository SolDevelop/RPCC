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
file = pathlib.Path("setup.key")
import ctypes
import webbrowser
import signal
import re
import pyautogui

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if oss == "Windows":
       if sys.argv[1] == "-setup":
         if not file.exists():
           if is_admin():
                os.system("netsh advfirewall firewall add rule name=\"SHORTCUT 80\" dir=in action=allow protocol=TCP localport=80")

                E = open("setup.key", "w+")
                E.write("" + oss)
                E.close()
                sys.exit()
           else:

              ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
         else:
            print("You Already Setup it")
       elif sys.argv[1] == "-run":


           layout = [[sg.Text('Please Enter The IP that the Server will be running on')],
    [sg.Text('IP Address:', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()],[sg.Text('')]]
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
                        os.remove("run.key")
                        run = open("run.key", "w+")
                        run.write("R")
                        run.close()
                        evente = windowd.read()
                        windowd.close()
                        if evente == "Exit" or evente == sg.WIN_CLOSED:
                             os.remove("run.key")
                             run = open("run.key", "w+")
                             run.write("N")
                             run.close()
                             sys.exit()
                             break
       elif sys.argv[1] == "-load":
           if sys.argv[2] == "sc":
              run = open("run.key", "r")
              if run.readline() == "R":
                 with open("load.key", "rt") as load:
                      for line in load:
                          key = json.loads(line)
                 LC = key[str(oss)][0]
                 SV = LC['SC']
                 if SV == "true" or SV == "True":
                      P = os.getcwd()
                      FP = P + "\\screenshot.png"
                      RFP = r'' + FP
                      SC = pyautogui.screenshot()
                      SC.save(RFP)
                      print("./screenshot.png")
                 else:
                     print("SCNT")
           elif not sys.argv[2] == "command":
             with open('load.key', 'rt') as load:
                for line in load:
                    key = json.loads(line)
             run = open("run.key", "r")
             if run.readline() == "R":
                WTO = sys.argv[2]
                CV = key[str(oss)][0]
                if WTO in CV:
                   Run = CV[str(WTO)]
                   subprocess.call([Run])
                   print("Done! " + WTO  + " Is Running!")
             else:
               print("The Server Isnt Running!")

           else:
               run = open("run.key", "r")
               if run.readline() == "R":
                 with open("command.key", "rt") as CK:
                     for line in CK:
                        CO = json.loads(line)
                 commandencode = sys.argv[3:]
                 CP = sys.argv[3]
                 CCP = CO[str(oss)][0]
                 if CP in CCP:
                   unlist = ' '
                   command = unlist.join(commandencode)
                   subprocess.Popen(str(command))
                   print("Done")
                 else:
                   print("Sorry But You Are Trying To Use Unallowed Command")
               else:
                   print("The Server Isnt Running!")




elif oss == "Darwin":
         if sys.argv[1] == "-setup":
             if not file.exists():
                 os.system("sudo nc -l 80")

                 E = open("setup.key", "w+")
                 E.write("Setup Completed\n OS: " + oss)
                 E.close()
                 sys.exit
             else:
                 print("You Already Setup it")
         elif sys.argv[1] == "-run":

             layout = [[sg.Text('Please Enter The IP that the Server will be running on')],
                       [sg.Text('IP Address:', size=(15, 1)), sg.InputText()],
                       [sg.Submit(), sg.Cancel()],
                       [sg.Text('')]]
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
                         t = "sudo php -S " + values[0] + ":80"
                         proc = subprocess.Popen(t, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                         os.remove("run.key")
                         run = open("run.key", "w+")
                         run.write("R")
                         run.close()
                         evente = windowd.read()
                         windowd.close()
                         if evente == "Exit" or evente == sg.WIN_CLOSED:
                             os.remove("run.key")
                             run = open("run.key", "w+")
                             run.write("N")
                             run.close()
                             os.system("kill " + proc.pid)
                             sys.exit()
                             break
         elif sys.argv[1] == "-load":
             if not sys.argv[2] == "command":
               with open('load.key', 'rt') as load:
                  for line in load:
                      key = json.loads(line)
               run = open("run.key", "r")
               if run.readline() == "R":
                   WTO = sys.argv[2]
                   CV = key[str(oss)][0]
                   if WTO in CV:
                       Run = CV[str(WTO)]
                       os.system("open " + Run)
                       print("Done! " + WTO + " Is Running!")
               else:
                 print("The Server Isnt Running!")
             else:
              run = open("run.key", "r")
              if run.readline() == "R":
                  with open("command.key", "rt") as CK:
                      for line in CK:
                          CO = json.loads(line)
                  commandencode = sys.argv[3:]
                  CP = sys.argv[3]
                  CCP = CO[str(oss)][0]
                  if CP in CCP:
                      unlist = ' '
                      command = unlist.join(commandencode)
                      subprocess.Popen(str(command))
                      print("Done")
                  else:
                     print("Sorry But You Are Trying To Use Unallowed Command")
              else:
                  print("The Server Isnt Running!")
elif oss == "Linux":
         if sys.argv[1] == "-setup":
             if not file.exists():
                 print("")
                 os.system("sudo firewall-cmd --add-port=80/tcp")

                 E = open("setup.key", "w+")
                 E.write("Setup Completed\n For OS: " + oss)
                 E.close()
                 sys.exit
             else:
                 print("You Already Setup it")
         elif sys.argv[1] == "-run":

             layout = [[sg.Text('Please Enter The IP that the Server will be running on')],
                       [sg.Text('IP Address:', size=(15, 1)), sg.InputText()],
                       [sg.Submit(), sg.Cancel()],
                       [sg.Text('')]]
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
                         t = "sudo php -S " + values[0] + ":80"
                         proc = subprocess.Popen(t, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                         os.remove("run.key")
                         run = open("run.key", "w+")
                         run.write("R")
                         run.close()
                         evente = windowd.read()
                         windowd.close()
                         if evente == "Exit" or evente == sg.WIN_CLOSED:
                             os.remove("run.key")
                             run = open("run.key", "w+")
                             run.write("N")
                             run.close()
                             proc.terminate()
                             sys.exit()
                             break
         elif sys.argv[1] == "-load":
             with open('load.key', 'rt') as load:
                 for line in load:
                     key = json.loads(line)
             run = open("run.key", "r")
             if run.readline() == "R":
                 WTO = sys.argv[2]
                 CV = key[str(oss)][0]
                 if WTO in CV:
                     Run = CV[str(WTO)]
                     os.system(Run)
                     print("Done! " + WTO + " Is Running!")
             else:
                 print("The Server Isnt Running!")

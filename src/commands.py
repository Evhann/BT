# /BT/src/commands.py
from os import name, system
import datetime

commands = ["echo", "mkdir", "cd", "rm", "rmdir", "ls", "date", "clear", "cat", "guiinit", "pide", "calc"]

def echo(text: str):
    print(text)

def mkdir(dir: str):
    pass

def cd(dir: str):
    pass

def rm(file: str):
    pass

def rmdir(dir: str):
    pass

def ls():
    from os import listdir
    for i in listdir():
        print(i, end=" ")
    print("")

def date():
    print(datetime.date.today())

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def cat(file: str):
    from os.path import isfile
    if isfile(file):
        with open(file, "r") as f:
            print(f.read())

def guiinit():
    from os.path import isdir
    if isdir("gui"):
        with open("gui/g.i", "w") as f:
            f.write("// this file is just to know if the user got the gui folder")
    else:
        print("Can't initialize gui.")
        print("Please download the gui module.")

def pide():
    from os.path import isfile, isdir
    if isfile("gui/g.i"):
        if isdir("gui/pide"):
            from os import name, system
            if name == 'nt':
                system("python gui/pide/src/main.pyw")
            else:
                system("python3 gui/pide/src/main.pyw")
    else:
        guiinit()
        print("Please restart pIDE.")

def calc():
    from os.path import isfile, isdir
    if isfile("gui/g.i"):
        if isdir("gui/calc"):
            from os import name, system
            if name == 'nt':
                system("python gui/calc/src/main.pyw")
            else:
                system("python3 gui/calc/src/main.pyw")
    else:
        guiinit()
        print("Please restart calc.")
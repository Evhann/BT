# /BT/src/commands.py
import os, datetime, os.path, shutil

commands = ["echo", "mkdir", "cd",
            "rm", "rmdir", "ls",
            "date", "clear", "cat",
            "guiinit", "pide", "calc",
            "btver", "file"]

def echo(text: str):
    print(text)

def mkdir(dir: str):
    if os.path.isdir(dir):
        print("Directory already exists.")
    else:
        os.mkdir(dir)
        print(f"Directory \"{dir}\" created.")

def cd(dir: str):
    os.chdir(dir)

def rm(file: str):
    if os.path.isfile(file):
        os.remove(file)
        print(f"File \"{file}\" removed.")
    else:
        print(f"File \"{file}\" doesn't exist.")

def rmdir(dir: str):
    if os.path.isdir(dir):
        shutil.rmtree(dir)
        print(f"Directory \"{dir}\" removed.")
    else:
        print(f"Directory \"{dir}\" doesn't exist.")

def ls():
    from os import listdir
    for i in listdir():
        print(i, end=" ")
    print("")

def date():
    print(datetime.date.today())

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cat(file: str):
    from os.path import isfile
    if isfile(file):
        with open(file, "r") as f:
            print(f.read())

def guiinit():
    from os.path import isdir
    if isdir("gui"):
        with open("gui/g.info", "w") as f:
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

# get windows username
def get_username():
    from getpass import getuser
    return getuser()
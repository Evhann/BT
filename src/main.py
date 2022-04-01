# /BT/src/main.py
from commands import *
from errors import *
from sys import exit
from colorama import Fore, Style
ver = "BT build 010422.1"


clear()
print(ver)
while True:
    command_input = input(f"{Fore.GREEN}?{Style.RESET_ALL}> ")
    command_input_split = command_input.split()
    current_command = command_input_split[0]
    match current_command:
        case "echo":
            echo(command_input[5:])
        case "mkdir":
            mkdir(command_input[6:])
        case "date":
            date()
        case "ls":
            ls()
        case "clear":
            clear()
        case "exit":
            clear()
            exit()
        case "cat":
            cat(command_input[4:])
        case "guiinit":
            guiinit()
        case "pide":
            pide()
        case "calc":
            calc()
        case "btver":
            print(ver)
        case default:
            pass
    if current_command not in commands:
        UnknownCommand(current_command)

from commands import *
from errors import *
from sys import exit
from colorama import Fore, Style
import threading

ver = "BT build 150522"
def interpreter():
    while True:
        command_input = input(f"{Fore.RED}?{Fore.GREEN}{get_username()}{Style.RESET_ALL}> ")
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
                exit(0)
            case "cat":
                cat(command_input[4:])
            case "guiinit":
                t = threading.Thread(target=guiinit)
                t.start()
            case "pide":
                t = threading.Thread(target=pide)
                t.start()
            case "calc":
                t = threading.Thread(target=calc)
                t.start()
            case "btver":
                print(ver)
            case "file":
                interpret_file(command_input_split[1])
            case "help":
                help()
            case default:
                pass
        if current_command not in commands:
            UnknownCommand(current_command)



def interpret_file(file_name):
    with open(file_name, "r") as file:
        rfile = file.read()
        lines = rfile.split("\n")
        for line in lines:
            command_input_split = line.split(" ")
            current_command = command_input_split[0]
            match current_command:
                case "echo":
                    echo(line[5:])
                case "mkdir":
                    mkdir(line[6:])
                case "date":
                    date()
                case "ls":
                    ls()
                case "clear":
                    clear()
                case "exit":
                    clear()
                    exit(0)
                case "cat":
                    cat(line[4:])
                case "guiinit":
                    t = threading.Thread(target=guiinit)
                    t.start()
                case "pide":
                    t = threading.Thread(target=pide)
                    t.start()
                case "calc":
                    t = threading.Thread(target=calc)
                    t.start()
                case "btver":
                    print(ver)
                case "help":
                    help()
                case "":
                    print("Warning: Don't put empty lines in your file.")
                case default:
                    pass
            if current_command not in commands:
                UnknownCommand(current_command)

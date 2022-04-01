# /BT/src/errors.py

def UnknownCommand(command):
    print(f"Command {command} doesn't exist.")

class NotEnoughPermissions(Exception):
    pass

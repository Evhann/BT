from interpreter import interpreter
import sys
from commands import clear

ver = "BT build 150522"
print(ver)

if len(sys.argv) > 0:
    if sys.argv[1] == "-nc" or sys.argv[1] == "--no-clear":
        pass
    if len(sys.argv) > 1:
        if sys.argv[1] == "-i" or sys.argv[1] == "--interpret":
            from interpreter import interpret_file
            interpret_file(sys.argv[2])
            sys.exit(0)
        
    else:
        clear()

try:
    interpreter() # start command interpreter
except KeyboardInterrupt:
    sys.exit(0)

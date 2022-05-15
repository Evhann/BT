from interpreter import interpreter
import sys
from commands import clear

ver = "BT build 150522"
print(ver)

if len(sys.argv) > 0:
    if sys.argv[1] == "-nc" or sys.argv[1] == "--no-clear":
        pass
else:
    clear()

try:
    interpreter() # start command interpreter
except KeyboardInterrupt:
    sys.exit(0)

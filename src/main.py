from interpreter import interpreter
import sys, infos
from commands import clear


if len(sys.argv) > 1:
    if sys.argv[1] == "-nc" or sys.argv[1] == "--no-clear":
        pass
    if len(sys.argv) > 2:
        if sys.argv[1] == "-i" or sys.argv[1] == "--interpret":
            from interpreter import interpret_file
            interpret_file(sys.argv[2])
            sys.exit(0)
else:
    clear()
    print(infos.ver)

try:
    interpreter() # start command interpreter
except KeyboardInterrupt:
    sys.exit(0)

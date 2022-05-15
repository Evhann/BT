from interpreter import interpreter
import sys

ver = "BT build 150522"
print(ver)

try:
    interpreter() # start command interpreter
except KeyboardInterrupt:
    sys.exit(0)

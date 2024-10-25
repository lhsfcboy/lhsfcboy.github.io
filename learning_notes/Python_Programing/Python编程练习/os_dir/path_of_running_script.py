import os
import sys


print('sys.argv[0] =', sys.argv[0])
print(os.path.dirname(sys.argv[0]))
print(os.path.abspath(os.path.dirname(sys.argv[0])))
print()

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.realpath(__file__)))
print()


print(sys.executable)

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

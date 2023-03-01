import sys

for key in sorted(sys.modules.keys()):
    print(key)

print('cmath' in sys.modules)
print('cmath' in globals())

from cmath import exp

print('cmath' in sys.modules)
print('cmath' in globals())
print('exp' in sys.modules)
print('exp' in globals())

from cmath import *

print(globals())
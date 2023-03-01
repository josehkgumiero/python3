import sys
print(sys)

import importlib
print(importlib)

print('math' in sys.modules())

importlib.import_module('math')

print('math' in sys.modules())

print('math' in globals())

math2 = importlib.import_module('math')

print('math2' in globals())

print(math2.__spec__)

print(sys.meta_path)

importlib.util.find_spec('decimal')


with open('module1.py', 'w') as code_file:
    code_file.write("print('running module1.py ...')\n")
    code_file.write('a=100\n')


impotlib.util.find_spec('module1')

import module1

print'module1' in globals())

print(module1.a)

import os

ext_module_path = os.environ['HOMEPATH']

print(ext_module_path)

file_abs_path = os.path.join(ext_module_path, 'module2.py')


with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...)\n")
    code_file.write("'x = 'python'\n")


importlib.util.find_spec('module2')

print(sys.path)

sys.path.append(ext_module_path)

importlib.util.find_spec('module2')

import module2

print(module2.x)
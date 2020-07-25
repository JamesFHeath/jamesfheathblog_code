#my_module.py
#---------------
print('Hello, World')

def print_searing_frost():
    print('SearingFrost')

print('End of Module')
#---------------

import json

python_dict = json.loads('{"key": true}')

#main.py
#---------------
import my_module

print('hello from inside main.py')

my_module.print_searing_frost()
#---------------

from json import loads

from json import loads, dumps

from json import * 


#main.py
#-------------
import my_module

print('hello from inside main.py')

if __name__ == '__main__':
    my_module.print_searing_frost()
#-----------------
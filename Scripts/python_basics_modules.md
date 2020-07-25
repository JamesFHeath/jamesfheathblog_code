# Introduction
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about modules in Python.
Python *modules* are just files with Python code in them. 
Python modules have the suffix *.py*. 
Definitions in modules can be accessed outside of the module using the *import* keyword. 


# Basic Module
Let's create a simple module. 

my_module.py
---------------
print('Hello, World')
def print_searing_frost():
    print('SearingFrost')
print('End of Module')
---------------

We can then run this statement from our terminal or command prompt with *python hello_world.py*. 
The Python interpreter *runs from top to bottom every statement in the module*.
Functions and classes are added to the interpreter as definitions, but we can see that the SearingFrost print statement is not executed because it's inside the function and not invoked. 

# Importing Modules
If you need code from other modules, it can be *imported*. 
Simply use the import statement followed by the module or package name. 
Standard library modules and packages are always available, such as math, json, and xml. 

import json
python_dict = json.loads('{"key": true}')
python_dict

Accessing submodules or specific definitions in a single module is accomplished with *dot* syntax
Here, we are creating a python dictionary using the json.loads method. 
json.loads() refers to a function named *loads* in the json module.
json.loads() takes a JSON string and returns the respective Python object

You can import definitions from your own modules as well. 
If the module is in the same directory, you can simply use *import my_module*.
Let's import the module we created earlier. (Show picture of module)
Simply import my_module, then we can invoke the print searing frost function. 
You'll also notice that the print statements from my_module are still run. 
When a module is imported, all statements are executed. 

my_module.py
---------------
print('Hello, World')

def print_searing_frost():
    print('SearingFrost')

print('End of Module')
---------------

main.py
---------------
import my_module

print('hello from inside main.py')

my_module.print_searing_frost()
---------------

# Importing with From
You can also import single definitions using the *from* keyword. 
The single definition will then be available in scope. 
Here we import loads from the json module, and it is the only function in scope. 
We can import multiple functions from the same module by separating the functions with commmas, here we import loads and dumps from json. 
Here we import every definition from the json module using an asterix, but this is discouraged.

from json import loads

from json import loads, dumps

from json import * 

# main function
Best practice for a module you want to run directly using the Python interpreter is using a main function.
It's different from some other languages that define a function called main. 
Python checks if the name of the module running is the string underscore underscore main underscore underscore.
If it is, then Python will run the code defined in the if block. 
We can easily add an *if \_\_name\_\_ == '\_\_mainj\_\_'* block to our main.py module. 
Keep in mind, this will Will STILL print "hello from inside main dot py" and also searingfrost from the if name = main block

main.py
-------------
import my_module

print('hello from inside main.py')

if __name__ == '__main__':
    my_module.print_searing_frost()
-----------------

# Thanks for Watching
Thanks for watching this introduction to modules in Python. 
Organizing your code into modules is an important part of software engineering, and will help you keep track of larger projects. 
Links to the code and my blog post on modules are in the description. 
I'll see everyone next time. 
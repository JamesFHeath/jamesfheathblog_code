# Introduction
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about packages in Python.
Python *packages* are a folder containing Python modules. 
Python packages just require an __init__.py file, often blank, inside of them to be recognized as a package. 
You can think of packages as a level up of organization from modules. 
Packages can even contain subpackages. 

# Importing Packages
To import packages, you use the import keyword to import the definitions from the package's \_\_init\_\_.py or from modules inside the package. 
Dot notation is used to get to subpackages and definitions within modules. 
We're going to import from the package defined here. 
You can import the entire package.
And also modules inside the package
And also subpackages inside the package
From imports work as well
It can get a little complicated if your package has a lot of levels.

import my_package

import my_package.my_module

import my_package.my_subpackage_1

from my_package import my_module

from my_package.my_subpackage_1 import my_submodule_1

# Creating your own Packages
To create our own packages, we'll be following the Python documentation on creating packages linked in the description. 
First we need to create a few files. 
The most important is setup.py, as it defines the metadata for our package. 
(Show contents of setup.py, many screenshots with different parts highlighted)
It includes things like author name, other libraries needed to install, and the package version. 
The sample package is linked in the description.
You simply install it by running pip install on the setup.py directory.
Then you just import like any other package. 

pip install /path/to/PythonBasicsPackage/

from PythonBasicsPackage import sample_module

sample_mdoule.hello_world()

python run_package.py

# Thanks for Watching
Thanks for watching this quick introduction to packages in Python. 
Understanding how to use and create packages will help organize your projects and help you use various libraries with ease. 
Links to the code and my blog post on packages are in the description. 
I'll see everyone next time. 
LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-grab-bag-virtual-environments.html
Commands: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Grab%20Bag/virtual_envrionments.sh
Python Virtual Environment Documentation: https://docs.python.org/3/tutorial/venv.html

# Intro
Hi Everyone, SearingFrost here with another Python Basics Video.
Today we're going to dig into the Python grab bag and pull out virtual environments. 

Virtual environments are a way of isolating specific Python resources for a project. 
Virtual environments have their own Python interpreter, pip, and installed libraries. 
Virtual envrionments can be activated and deactivated on the command line or terminal
This allows you to work on projects that need certain defined resources. 

# Creating a Virtual Envrionment
We'll be using bash, which will work on Linux or Mac
I've linked my blog post and the python virtual environment docs in the description if you need Windows instructions. 
Virtual environments can be created anywhere on the file system, a reasonable location is an venvs directory in your home directory.
Let's create our virtual environments directory and change to it
Now we will create a virtual environment named "searing-frost" using the venv module.
This module is package with all recent python versions. 
searing-frost is now a directory that contains several other directories. 

mkdir ~/venvs
cd ~/venvs
python3 -m venv searing-frost
cd searing-frost
ls

# Activating and Deactivating Virtual Environments
The **bin** directory contains the script to activate the virtual environment. 
All we need to do is run source...bin...activate
Once the virtual environment is activated, the terminal will show (searingfrost) on the prompt.
To leave the virtual environment, just use **deactivate**

source ./bin/activate

deactivate

# Installing and Packaging Libraries in Virtual Environments
The virtual environment has its own pip that you can use to install libraries. 
Let's see what's installed by default with **pip list**. 

(searing-frost)~/venvs/searing-frost$ pip list

If we install a new library, it will install only to the virtual environment's **site-packages**, not system wide. 
Let's install numpy...
Pip has added it to the searing-frost virtual environments site packages 

pip install numpy
pip show numpy
pip list


Now that we have a version of numpy, we need to share it with a requirements.txt file.
A requirements.txt file for the project related to the virtual environment can be created easily with **pip freeze**.
Package the requirements.txt with the project source code so everyone can install the same version of libraries. 

pip freeze
pip freeze > ~/searing-frost-project/requirements.txt
cat ~/searing-frost-project/requirements.txt

# Thanks for Watching
Thanks for watching this video on virtual environments. 
Virtual environments will come up often when working on larger projects with other people. 
It's important to understand how they work in order to work effectively. 
Links to my blog post on decorators and the video commands are in the description. 
I'll see everyone next time. 

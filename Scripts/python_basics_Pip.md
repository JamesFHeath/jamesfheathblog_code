# Introduction
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about Pip.
Pip is the default Python package manger.
It allows you to install Python libraries to your computer so they can be imported into your Python code. 
Pip comes packaged with Python since 3.4, but you can also manually install it with a script. 
Links to downloading and installing Python and Pip are in the video description. 


# Installing 3rd Party Libraries with Pip
Let's try to install a common Python library called Pandas, it's a library for data analysis and transformation. 
If you want to find more libraries, PyPi is the place. (Show searching for pandas on Pypi) 
Once pip is installed on your computer and added to your path, simply run the command pip install pandas
Then pandas is available for import.
Updating packages is simple, just specify upgrade in your argument to pip
Uninstalling is just as easy
You want to upgrade pip itself from time to time, just install use the upgrade flag on pip.

pip3 install pandas

import pandas

pip3 install --upgrade pandas

pip3 uninstall pandas

pip3 install --upgrade pip

# Installing Your Own Packages with Pip
If you have your own package built locally, you simply install it by running pip install on the setup.py directory.
Check out my video on packages for details.

pip install /path/to/package/

# Other Pip Utilities
You can see all your installed libraries with *pip list*.
pip list


You can also see specifics about a single library, such as version, dependencies, and install location, with *pip show*
pip show pandas


# Requirements.txt
If you're working on a project, especially one with other people, you want to make sure you're all using the same libraries.
*Requirements.txt* files define which libraries your Python project needs. 
You can define package names and versions in requirements.txt, and use pip to install them. 
Just use the recursive flag and it will go line by line and install all the libraries for you. 

requirements.txt
-----------------
pandas==1.0.5
boto3
-----------------

pip3 install -r requirements.txt


# Thanks for Watching
Thanks for watching this quick introduction to Pip in Python. 
Using pip is your key to a world of amazing python libraries. 
Productivity is king in Python, and an abundance of libraries for machine learning, data transofmration, web servers, almost anything exist out there. 
Links to the code and my blog post on pip are in the description. 
I'll see everyone next time. 
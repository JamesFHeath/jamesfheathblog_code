# Intro
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about files in Python.
Python has a ton of great utilities for working with files, especially text files. 
We're going to go over the basics of reading from files and writing to files in this video. 


# Reading from Files
Reading from files in Python is very easy using the **with** keyword. 
**With** lets Python take care of the business of opening and closing our files, and we can just focus on getting our work done. 
The **open** function takes a file path and opens the file for you in the **with** context. 
Here we open my_file.txt and assign the file handler to the variable my_file
We then read the contents to file_contents

with open('my_file.txt') as my_file:
    file_contents = my_file.read()
file_contents

There are several ways to read the contents of a file, the most common will be the file.read() method and iteration. 
THe read method reads all the file's contents to a variable. 
We can also iterate line by line with a for loop
Here we open my_file again and print out the contents line by line

with open('my_file.txt') as my_file:
    for line in my_file:
        print(line)

# Writing to Files
Writing to files is just as easy in Python using the **with** keyword. 
You just need to specify in the **open** function that you want to write to the file with the mode argument. 
Specifying 'w' as the mode means write, it defaults to read only , which is an 'r'
Here we write the string 'SearingFrost to the file searingfrost.txt, then read the contents to see the result.

with open('searing_frost.txt', mode='w') as my_file:
    my_file.write('SearingFrost')

with open('searing_frost.txt') as my_file:
    searing_frost = my_file.read()

searing_frost

# Thanks for Watching
Thanks for watching this introduction to Files in Python. 
Links to the code and my blog post on files are in the description. 
I'll see everyone next time. 
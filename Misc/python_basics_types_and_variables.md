# Intro
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about types and variables. 
Types classify our objects in Python.  
Python uses a dynamic type system.
Dynamic type systems figure out the type of a variable at runtime.
Static type systems figure out the type of a variable at compile time. 
Dynamic languages include Python and Javascript.
Static languages include Java and C++. 

# Setting Variables
Variables in Python are set with the **=** operator. 
Because Python figures out the type of a variable at runtime, there is no need to add type signatures to variables. 
Once a variable is set, there is no restriction to setting a new value to the same variable. 
Here I'm just defining x as an int 5. 
Then I can redefine it as the string hello
Then again as a float 1.0
x = 5
x
x = 'hello'
x
x = 1.0
x

# Type Function
The builtin **type** function is a valuable piece of your Python toolbox. 
It will tell you the type of any variable. 
Here x is an int
And s is a string
The type of my_function is function
But if we evaluate my_function, it returns a string and the type becomes string
x = 5
type(x)
s = 'hello'
type(s)
def my_function():
    return 'SearingFrost'

type(my_function)
type(my_function())

# Id Function
A very useful tool is the builtin **id** function. 
It takes a variable and returns the id of its memory location as just a number. 
You can use this to compare different variables to see if they are pointing to the same memory. 

Here I define list 2 as list 1, and their ids are equal. 
l1 = [1, 2, 3]
l2 = l1
id(l1) == id(l2)

Here the two dictionaries have the same values, but different memory locations
d1 = {'key': True}
d2 = {'key': True}
id(d1) == id(d2)

Primitives like ints and *None* are special, in that they have their own memory location that's loaded and can't be overwritten. 
Here x and y have equal ids
x = 5
y = 5
id(x) == id(y)

# Thanks for Watching
Thanks for watching this quick introduction to Types and Variables in Python. 
Python's type system is incredibly flexible and we've only scratched the surface here. 
Links to the code and my blog post on types and variables are in the description. 
I'll see everyone next time. 
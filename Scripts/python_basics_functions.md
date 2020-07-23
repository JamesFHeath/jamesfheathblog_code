# Introduction
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about functions in Python.
Functions in Python are the basic building blocks of structure for your programs. 
Python functions organize parts of code together, and allow you to easily run the same code many times. 
Python functions are also **first class citizens**, this means that functions can be treated as any other objects like being assigned to variables or even passed as arguments to other functions. 


# Defining Functions
Functions are defined in Python using the **def** keyword. 
The signature is **def** *my_function_name* and a list of arguments or parameters
The next line will be indented and have your function code. 
Values are returned from functions with the **return** keyword. 
If the **return** keyword is omitted, then a value of None is returned. 

def my_function(arg1, arg2):
    return arg1 + arg2

def my_none_function():
    print('hello')



# Calling Functions
Functions are called by typing the function name, then open parentheses around the arguments you want to pass in. 

def my_function(arg1, arg2):
    return arg1 + arg2

return_value = my_function(1, 1)
return_value


# Default Parameters
Function arguments can have defaults. 
You just need to set the arguments equal to any value you want. 
The result with the default values is 3.
If you overwrite the defaults, the function will operate on your parameters.
In this case, 4 and 5 give us 9

def my_function(arg1=1, arg2=2):
    return arg1 + arg2


return_value = my_function()
return_value

return_value = my_function(4, 5)
return_value


# Passing Functions as Parameters
When you reference a function name without parentheses, you can take the function and pass it around. 
For example, my_list_mutators takes takes another function as a parameter and applies it to every item in a list.
When we pass in  my_double_function without parentheses it's not evaluated until it's inside my_list_mutator

def my_list_mutator(arg_list, arg_function):
    new_list = []
    for arg in arg_list:
        new_list.append(arg_function(arg))
    return new_list

def my_double_function(x):
    return x * 2

doubled = my_list_mutator([1, 2, 3], my_double_function)
doubled

# Lambdas
Lambdas are anonymous functions, functions without names, that can be defined for quick purposes such as list comprehensions. 
They are defined with the lambda keyword, then parameters, then a colon that defines the return value.
For example This lambda function will take an argument, double it, and return the new value. 
Here we pass the value 5 as the argument and our result is 10
(lambda x: x * 2)
(lambda x: x * 2)(5)

Going back to our list doubling example, it's much nicer with a list comprehension and lambda
doubled = [(lambda x: x * 2) for x in [1, 2, 3]]
doubled

This can be made more compact with some syntatic sugar for list comprehensions
doubled = [x * 2 for x in [1, 2, 3]]
doubled

# Thanks for Watching
Thanks for watching this introduction to Functions in Python. 
Functions are the basic building blocks of Python programs.
Use them liberally. 
Links to the code and my blog post on functions are in the description. 
I'll see everyone next time. 
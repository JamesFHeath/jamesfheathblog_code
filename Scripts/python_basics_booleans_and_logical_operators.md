# Introduction
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about booleans and logical operators in Python.
In Python, booleans are a type with two values, *True* or *False*. 
They can be operated on and queried with functions like *if*, *and*, *or*. 
Python also has a sense of *truthy* and *falsey* values, values that will act as true or false when given to if statements. 

# Working with Booleans
Python uses *if*, *elif*, and *else* to execute code based on boolean values. 
*if* and *elif* preceede an expression that evaluates to a boolean value, and execute the code indented below them if the value is True. 
*else* blocks of code will execute if all *if*s and *elif*s failed. 

Python uses the words *and*, *or*, and *not* for logical and, or, and not, as opposed to other languages that use symbols. 

Boolean values can be assigned to variables and returned from functions just like any object. 
Then we can operate on the variables. 
And call this function to get a boolean value True

if True:
    print('True')
elif False:
    print('Won't Print')
else:
    print('Won't Print')

True and True
False or True
not False and True
True and False

true_variable = True
false_variable = False

true_variable and true_variable

false_variable or false_variable

def returns_true():
    return True

returns_true()

# Truthy and Falsey
Boolean operators can also work on non boolean values. 
Usually *empty* objects will evaluate to False, while objects that aren't empty will evaluate to True. 

(Screenshot this)
* Strings: "" == False, any string over length 0 == True
* Lists: [] == False, any list over length 0 == True
* Integers: 0 == False, any other number is True
* None: None will evaluate to False, this is helpful when testing for any return value

Truthy and falsey values are useful for checking for the existence of objects. 
Let's define a function to determine if a value is empty so we can see this in action.
The string SearingFrost is a truthy
But the empty string is a falsey value
Likewise the int 5 is truthy
But the int 0 is falsey

def truthy_or_falsey(value):
    if my_value:
        print('Truthy Value Found')
    else:
        print('Falsey Value Found')

searing_frost = 'SearingFrost'
truthy_or_falsey(searing_frost)

empty_string = ''
truthy_or_falsey(empty_string)

truthy_or_falsey(5)

truthy_or_falsey(0)

# Thanks for Watching
Thanks for watching this introduction to booleans in Python. 
Links to the code and my blog post on booleans and logical operators are in the description. 
I'll see everyone next time. 
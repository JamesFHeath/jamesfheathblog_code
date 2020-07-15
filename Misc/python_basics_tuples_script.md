# Intro
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about tuples. 
Tuples are basic collections in Python.
They store objects that are accessible through indexes and iteration. 
Tuples are very similar to lists, except that tuples are immutable. 
This means that once the value(s) of a tuple are set, they cannot be changed. 
Tuples also have a wonderful property called *unpacking*, which allows easy assignment of tuple values to variables. 


# Creating Tuples
There are 2 ways to create tuples in Python.
## Parentheses and Commas
Parentheses and commas are the simples way to create tuples. 
Just open parenthesis, add your values separated by commas, and close parenthesis. 
t = (1, 2, 3, 'hello')
t
Easy as that
## Built in Tuple Function
There is also a built-in tuple function that transforms any iterable to a tuple.
Just pass any iterable, like a list, to the tuple function.
l = [1, 2, 3]
t = tuple(l)
t

# Accessing elements in a tuple
Elements of a tuple can be accessed by their index or with iteration. 
This is the exact same as any sequence, like lists. 

Using square brackets, we can get the zero indexed values of a tuple
t = ('a', 'b', 'c')
t[0]
t[1]

but remember we can't reassign tuple values, as tuples are immutable
t[0] = 'banana'
error 

We can also iterate over a tuple with a for loop
for item in t:
    print(item)

# Tuple Unpacking
You're probably wondering why we are bothering with tuples when lists do the same and more. 
Tuple unpacking is what makes them special. 
Tuple unpacking is assigning the items in a tuple to several variables at once.

For example, we can assign the values of our abc tuple to variables x, y, and z respectively
t = ('a', 'b', 'c')
x, y, x = t
x
y
z

Tuple unpacking is especially useful when returning multiple values from a function.
Let's define a function that returns a dummy HTTP response and a message

def dummy_server_call():
    return (200, 'success')
We have our function return a two-tuple of an HTTP code and a message

We can then access the code and message with separate variables very nicely
code, message = dummy_server_call()
code
message

Tuple unpacking is what makes tuples so useful. 

# Named Tuples
What if you want all the benefits of tuples, but with named fields like dictionaries? 
That's where named tuples come in

They are part of the collections library, so let's import them first.
from collections import namedtuple

We can then define an HTTP Response namedtuple
HttpResponse = namedtuple('HttpResponse', ['code', 'message'])

We can rewrite our dummy Http function with the httpresponse named tuple
def dummy_server_call():
    return HttpResponse(200, 'success')

We can access the values by their field names now, using dot syntax
response = dummy_server_call()
response.code
response.message

They can also be accessed just like normal tuples, using unpacking or indexes

# Thanks for Watching
Thanks for watching this introduction to tuples in Python. 
Tuples are the best way to get some immutability in Python, and tuple unpacking is a wonderful feature. 
I know you'll find many uses for tuples. 
Links to the code and my blog post on tuples are in the description. 
I'll see everyone next time. 
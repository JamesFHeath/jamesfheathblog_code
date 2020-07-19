# Intro
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about exceptions. 
Exceptions are how Python programs deals with things going wrong. 
Examples of exceptions are division by 0, operating on the wrong type, or missing values. 
It's important to know how to handle exceptions using try/except logic. 


# Handling Exceptions with Try/Except
Handling exceptions requires using the **try/except** keywords. 

First I'm attempting division by zero, and we get division by zero error 
Then I'm surrounding it with a try, and when there's an exception it runs my print statement.
We can put any logic in the except area, such as retrying failed code.

1/0
try: 
    1 / 0 
except:
    print('Exception')    

We can also access the specific exception raised in order to operate on it. 
Here I'm capturing the exception as the variable e, and printing it out. 
Capturing this output is great for logging. 

'hello' + 1
try:
    'hello' + 1
except TypeError as e:
    print(f'TypeError: {e}')


# Raising Exceptions
Sometimes you want to inform the caller of your code that something went wrong. 

First, let's define our function to operate on two variables that can be added together
If the types are not equal, we raise an exception
Let's call it when the types are the same, and we get our expected output. 
But when we call it with different types, we get an error along with our custom message.

def my_add_function(x, y):
    if type(x) != type(y):
        raise Exception('Both arguments must be of the same type')
    return f'{x} + {y} = {x + y}'        


z = my_add_function(1, 1)
z

a = my_add_function(1, 'chicken')

# Thanks for Watching
Thanks for watching this quick introduction to Exceptions in Python. 
Exceptions will happen, and preparing for them and handling them is vital. 
Links to the code and my blog post on exceptions are in the description. 
I'll see everyone next time. 
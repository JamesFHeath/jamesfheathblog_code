LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-grab-bag-decorators.html
Code: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Grab%20Bag/decorators.py
Tenacity: https://pypi.org/project/tenacity/

# Intro
Hi Everyone, SearingFrost here. 
Today we're going to dig into the Python grab bag and pull out decorators. 
Decorators are functions that take a function as a parameter and return a function.
Python has special syntactic sugar for decorators using the **@** symbol above function signatures.
Mutliple decorators can be used by separating them on multiple lines. 

Decorators are easier to understand with examples, we're going to build up a single decorator from simple to complex.  
This decorator is a basic function that takes a single parameter, f for function, prints decorated, and returns the function f. 
This is just a normal function, Python doesn't have any special syntax to define decorators. 
Let's define a function *to_decorate* that just prints To Decorate and returns 1
We can decorate our to_decorate function by placing AT decorator above the definition. 
When Python sees the *@decorator*, it actually immediately runs the function *decorator* with *to_decorate* passed as the first parameter
This is why 'Decorated!' prints immediately
When we run our function, we can see the output To Decorate, but we don't see Decorated print out. 
As mentioned before, This AT syntax is syntactice sugar for redefining to_decorate as the result of decorator with to_decorate passed as the only parameter. 
The result of this call is simply the function to_decorate returned from the decorator

def decorator(f):
    print('Decorated!')
    return f

@decorator
def to_decorate():
    print('To Decorate')
    return 1

to_decorate()

to_decorate = decorator(to_decorate)


What if we want to execute our decorator code when the decorated function is called, not immediately when decorated? 
This is where wrapper functions come in. 
Let's modify our decorator function. 
We can define a new function inside decorator called *wrapper*
This function will print Decorated, then execute the decorated function f
Our decorator now returns the wrapper function instead of our decorated function
Notice nothing is printed when decorated
And when we run our newly decorated function, we get the outputs Decorated and To Decorate
When we look at the equivalent syntax, decorator returns the function wrapper, but does not execute it

def decorator(f):
    def wrapper():
        print('Decorated!')
        f()
    return wrapper

@decorator
def to_decorate():
    print('To Decorate')
    return 1

to_decorate()

to_decorate = decorator(to_decorate)


What if our decorated function takes parameters, how can we access them inside the decorator? 
Remember, we are calling the wrapper function when we call **to_decorate()**, so if our function takes arguments, then wrapper can take arguments and pass them to our function when it calls f
Let's give wrapper a positional args tuple and a keyword args dictionary.
Then we can just pass those parameters to f directly.
Now we can modify our to_decorate funtion with some parameters, x, y and keywords. 
And we will just print them unmodified. 
Now we can pass some random parameters to our decorated function, and we can see the results output correctly. 
This can be a little confusing, but remember it's just a call to wrapper. 

def decorator(f):
    def wrapper(*args, **kwargs):
        print('Decorated!')
        f(*args, **kwargs)
    return wrapper

@decorator_with_wrapper
def to_decorate(x, y, **kwargs):
    print('To Decorate')
    print(x)
    print(y)
    print(kwargs)
    return 1

to_decorate('searingfrost', 'another parameter', **{'key': 'value'})

to_decorate = decorator(to_decorate)

Additional parameters can also be passed to the decorator function itself. 
We need a new pattern to accomplish this, the decorator factory. 
The syntactice sugar here is a little different.
Decorator factories will be passed the arguments in the AT decorator signature, then they will return a decorator. 
Let's add a decorator factory around our decorator function that takes positional and keyword args. 
We can then access these arguments inside the decorator and wrapper functions. 
Let's just output the parameters so we can see how this works. 
We can pass in parameters to the decorator factory when we decorate our function, and they work just like normal function parameters. 
We can see the output is what we were hoping for. 
Breaking down the syntactic sugar, we can see that two separate function calls are made.
The first call returns decorator from decorator_factory
And the second call returns wrapper just as before. 


def decorator_factory(*factory_args, **factory_kwargs):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print(f'Args Passed to factory: {factory_args}')
            print(f'KeywordArgs passed to factory: {factory_kwargs}')
            print('Decorated!')
            f(*args, **kwargs)
        return wrapper
    return decorator_with_wrapper

@decorator_factory('someargument', a=5, b=10)
def to_decorate(x, y, **kwargs):
    print('To Decorate')
    print(x)
    print(y)
    print(kwargs)

to_decorate('searingfrost', 'another parameter', **{'key': 'value'})

to_decorate = decoratory_factory('someargument', a=5, b=10)(to_decorate)


# Thanks for Watching
Thanks for watching this tutorial on decorators. 
Decorators are a bit confusing when you first start working with them. 
Play around with the syntax, and follow the chain of execution so you can understand what is happening. 
Decorators are used for tons of purposes, one of my favorite examples is the tenacity library for retrying code after exception, which I have linked in the video description. 
Another common use case is a logging facility for logging decorated functions and their parameters automatically. 
Basically, anywhere you have generic behavior you want your functions to perform, a decorator could be a good choice. 
Links to my blog post on decorators and the video code are in the description. 
I'll see everyone next time. 

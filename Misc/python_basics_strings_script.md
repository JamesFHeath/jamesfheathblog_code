# Intro
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about strings. 
Strings are one of the basic data types in Python. 
Strings are sequences of Unicode pointers, as of Python 3.
Strings can be accessed using iteration and indexes just like lists. 
Like tuples, strings are immutable. 
A string's value cannot change once assigned. 
Unlike other languages, Python has no concept of characters or chars. 
In many languages, strings are just arrays of characters. 
In Python, a single element of a string is simply a string of length 1. 

# Creating Strings
Strings can be created as string literals or using the builtin str function. 
## String Literals
String literals are surrounded with single quotes ', double quotes ", or 3 single ''' or 3 double quotes """.
*Type as you're talking*
s = 'hello'
s2 = "hello"
s3 = '''hello'''
s4 = """hello"""
These are all equivalent strings

The *str* function takes any object and returns a string. 
It will cast any other type into a string for you using the object's str method
int_five = 5
str_five = str(5)
str_five

d = {'key': 55}
str_d = str(d)
str_d


### Accessing Elements
String elements are accessed exactly like lists. 
s = 'hello'
s[0]
But just like tuples, they are immutable so you can't set their values
s[4] = 't'

You can also access strings with slices using a start and end index
s[0:2]

Check my video on lists for more details on accessing sequences

# String Methods
Strings have tons of builtin methods, I'm going to touch on a few of the ones I most commonly use.
Check the documentation in the description for a full list. 
Concatenation is simply putting two strings together to create a new string. 
Just use the + operator to use this method. 
s1 = 'hello '
s2 = 'world'
s3 = s1 + s2
s3

The replace method replaces instances of a search string with a replacement string and returns a new string. 
s1 = 'SearingFrost'
s2 = s1.replace('Frost', 'Fire')
s2

The split method splits a string based on a given delimiter, such as a comma, a returns a list of the sub strings.
s1 = 'Searing, Frost, Fire'
l = s1.split(',')
l


# String Formatting
String formatting is a method that creates strings out of other types. 
I'm going to be using the *f* string formatting only, as it's just the best one.
To create an *f string*, or format string, simply add a lowercase f before the first quotaion. 
You can then use curly brackets to surround ANY Python expression you want evaluated as a string. 
This is known as interpolation.
sf = 'Searing Frost'
f_string = f'Hello, my name is: {sf}'
f_string

expression_string = f'1 + 1 = {1 + 1}'
expression_string
F strings are just incredibly useful for outputting formatted text, especially when writing to log files. 

# Thanks for Watching
Thanks for watching this introduction to Strings in Python. 
Strings are used constantly in Python. 
Python has tons of advanced features for manipulating strings and parsing text. 
We've only scratched the surface here, but I would always recommend Python first whenever you need to work programatically on any text.
Links to the code and my blog post on tuples are in the description. 
I'll see everyone next time. 
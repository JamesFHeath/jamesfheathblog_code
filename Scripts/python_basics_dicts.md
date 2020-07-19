# Intro
Hi Everyone, SearingFrost here with another Python Video.
Today, we'll be talking about dictionaries. 
Dictionaries, or dicts, are key-value collections in Python. 
Using only dictionaries, you can get really far writing Python.
They are the do-it-all data structure. 
Dictionaries can hold values of any type, but they keys have to be "hashable".
"Hashable" basically means immutable, only objects that can't change value can be keys
Key examples: integers, strings and even tuples
Strings are the most common key used because of their versatility. 



# Creating Dictionaries
There are 3 ways to create dictionaries in Python, much like lists. 
## Curly Brackets
Curly brackets are the simples way to create dictionaries. 
OPen curl brackets, following by key colon value, separated by commas. 
For example
d = {'key': 'value', 'another_key': 'another_value'}
d
## Built in Dict Function
There is also a built-in dict function that I don't use often. 
It takes any mapping, like another dictionary, a zip of key/value iterables, an list of pairs such as tuples, or keyword arguments. 
It really can take a lot of different types. 
Going over a few quickly, check the code links in the description for a closer look. 
### Using Zip on Two iterables:
You can create a list of keys and a list of values, and combine them using the builtin zip function. 
key_list = [1, 2, 3]
value_list = [True, True, False]
d = dict(zip(key_list, value_list))
d
### Using another dictionary
Just pass any other dictionary
d2 = dict(d)
d2
### Using an iterable of tuples
Here we have a list of two-tuples, and they will form the key/value pairs of the dictionary. 
tuple_d = dict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
tuple_d
### Keyword args
Here the arg name will be the key as a string, and the value is whatever you want. 
keyword_d = dict(key1='value1', key2='value2', key3='value3')
keyword_d
## Dictionary comprehensions
Dictionary comprehensions are used much less than list comprehensions, but there are times when they are useful. 
Dictionary comprehensions are curly brackets, then a key/value pair, then a for variable in iterable with an optional filter. 
This comprehensions will give us the odd numbers smaller than 10 as keys and the value will be the key plus 100
dict_comprehensions = {x: x * 100 for x in range(10) if x %% 2 == 1}
dict_comprehension



# Adding Values to Existing Dictionaries
You can add values with square brackets or the update method. 
Using square brackets, you specify a key and *=* to define the value of that key.
d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
Here we add a new key
d['3rd Key'] = True
d
Here we replace an existing key with a new value
d['my_key'] = 'new value'
d

Using the *update* method, you can add values to your dict with the same arguments the dict function takes. 
Here's a keyword args examples. 
d = dict(key1='value1', key2='value2', key3='value3')
d.update(key4='value4')
d


# Accessing Values in Dicttionaries
Dictionary values can be accessed using key names. 
You can use square brackets just like with lists, but instead of putting in the index, you put in the key. 

d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
d['my_key']
If the key is not present, you will get a KeyError. 
d['my_missing_key']
To avoid this, you can use the *get* method. 
It will either return None, or a default value you specify.
d.get('my_missing_key')
d.get('my_missing_key', 'key missing!!!!')
You can also use the *in* operator to see if a key exists before trying to access it
'missing_key' in d
# False
'my_key' in d
# True

# Iteration with Dictionaries
The *in* operator can be used to access the keys of a dict. 
This way, you can access all the values of your dict. 

d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
for k in d:
    print(d[k])
If you want to access the keys AND values, you can use the items method. 
for k, v in d.items():
    print(k)
    print(v)

# Removing Keys from Dictionaries
To remove values from dicts, you can either use the *del* keyword, or the *pop* method.

{% highlight python%}
d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
del d['my_key']
d
d.pop('my_other_key')
d

# Default Dictionary Bonus
Default dicts are actually subclasses of dictionaries that contain default values. 
They are defined with a type, such as *list* or *int*. 
When you access keys, if they key does not exist the value defaults to the empty constructor of the type passed in. 
It's easier to understand with an example. 

Be sure to import defaultdict from collections, part of the standar library
from collections import defaultdict

What if you want a dictionary of lists you want to append to, you can always use the append method with a default dictionary even if the key does not exist yet. 
dd = defaultdict(list)
dd['new'].append(1)
dd['new'].append(2)
dd

Another use case is with counters. 
If you want to count the appearances of items in a list, you can create a defaultdict of int.

If I want a dictionary to store word counts, I can iterate through the list and update counter values
word_list = ['Python', 'Blog', 'Python', 'Python', 'Dict', 'Dict']
count_dict = defaultdict(int)
Using int as the argument to defaultdict, the initial value will be ZERO

for word in word_list:
    count_dict[word] += 1
count_dict
Even though it may look slightly different, defaultdicts work just like normal dictionaries. 

# Thanks for Watching
Thanks for watching this introduction to dictionaries in Python. 
They really are, in my opinion, the most flexible and important data structure in the language. 
Knowing how to use dictionaries allows you to solve almost any problem. 
Links to the code and my blog post on dictionaries are in the description. 
I'll see everyone next time. 
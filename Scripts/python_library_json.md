LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-library-json.html
Code: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Libraries/json.py

# Intro
Hi Everyone, SearingFrost here in the Python Library.
Today we'll be checking out the JSON library, which is part of the standard library. 

# JSON
JSON is JavaScript Object Notation, and it is a data interchange format used widely on the web and elsewhere. 
The nature of JavaScript is dynamic, and Python works well for parsing and working with JSON. 
The standard library of Python has a wonderful JSON module that makes working with JSON simple. 

# JSON to Python
JSON maps nicely to Python objects when parsed. When translating Python to JSON, this process is reversible. However, more complex Python objects like datetime or namedtuples will not translate without custom behavior specified. 
Here is a table of some translations

| JSON | Python |
|:------|:--------|
| String | String |
| Number | Int or Float |
| Object | Dictionary |
| Array | List |
| null | None |
| true | True |
| false | False |

# Loads and Dumps
loads: parses a string of JSON into a Python object
dumps: serializes a Python object into a string of JSON

The main operations used with the JSON library are **loads** and **dumps**. 
**loads** takes in a String of JSON and parses it into the corresponding Python objects. 
**dumps** is the reverse, it takes a Python object and serializes it into a string of JSON. 
You'll often receive JSON responses from web servers and parse them with **loads**. 
Then you can create a Python object and stringify it with **dumps** to send back.  
First we just import json
Then we can create a string of some JSON, let's adds keys, and an array and a boolean.
I like using single quotes, especially for JSON strings because then you don't need to escape double quotes
We can then use json.loads to get the equivalent python object
Now we can operate on the Python object with our normal Python syntax. 
We can add a new key
Or append to the array, which is now a Python list
Once we are done, we can create a new JSON string using json.dumps and passing in the python object
And it result in the JSOn version of our python object

import json

json_string = '{"key": "value", "array_key": [1, 2, 3], "another_key_for_boolean": false}'

python_object = json.loads(json_string)
python_object


python_object['new_key'] = None
python_object['array_key'].append(4)
python_object

new_json_string = json.dumps(python_object)
new_json_string

Another other nice features of **dumps** is the ability to pretty print with the *indent* parameter. 
Just specify a number for the indentation, and the JSON string will be nicely formatted for human readable output. 
Let's create a simple python dictionary, then output it with an indent of 4.

import json

python_object = {'parent': {'child_1': [1, 2, 3], 'child_2': True}}

json.dumps(python_object, indent=4)


# Overriding default dumps behavior
Some objects are not directly translatable into JSON. 
**datetime** objects are a great example and will come up often. 
Let's create a datetime object of now
Then let's try to turn it into JSON with json.dumps. 
Unfortunately we get a type error because datetime objects aren't JSOn serializable

import datetime

now = datetime.datetime.now()
now

json.dumps(now)

The solution to creating JSON strings with **datetime** and other complex objects is to subclass the **JSONEncoder** class and implement a **default** method that returns a Python object that *can* be encoded. 
First we need to create a DateTimeEncoder that inherits from JSONEncoder.
Then we define our own default method that takes an object. 
We want to check only for datetime objects.
For our **datetime** object, let's turn it into a dictionary with a key of 'datetime_now' and a string representation of the datetime object, which *is* JSON serializable. 
Now we can create a DateTimeEncoder object and encode our datetime now object into JSON.

import datetime
import json

now = datetime.datetime.now()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) == datetime.datetime:
            return {'datetime_now': str(o)}
        return json.JSONEncoder.default(self, o)

date_time_encoder = DateTimeEncoder()

now_json_string = date_time_encoder.encode(now)

now_json_string

# Thanks for Watching
Thanks for joining me in the Python library for this look at json.
JSON is used basically everywhere on the web, and Python is a great tool for working with JSON. 
Links to the code and my blog post on json are in the description. 
I'll see everyone next time. 
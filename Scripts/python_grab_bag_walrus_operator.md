LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-grab-bag-walrus-operator.html
Code: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Grab%20Bag/walrus_operator.py
PEP 572: https://www.python.org/dev/peps/pep-0572/ 

# Intro
Hi Everyone, SearingFrost here. 
Today, we're going to reach into the python grab bag and pull out Assignment expressions, fondly called the **walrus operator**.
It is a new operator in **Python 3.8** that allows assigning the result of expressions to variables. 
***variable* := *expr*** can be placed anywhere an expression can be placed. 
The purpose of the walrus operator is to save the results of expressions that are going to be used in the future. 
In this video we're just going to go over a couple of examples to get the idea behind where walrus operators can be useful. 

#### Checking Values in a Dictionary
This first example will be checking if an object is in a dictionary, then using the value if it is in the dictionary. 
Let's define a simple dictionary first. 
Tradionally, we would check if the key is in the dictionary, then we can write some code to operate on the value of that key. 
With the walrus operator, we can check for the existence of the key and assign the value in one step. 

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Traditional way
if 'key1' in my_dict:
    value = my_dict['key1']
    print(value)

# Walrus Operator
if value := my_dict.get('key1'):
    print(value)

Let's now create a test value, and see if 'key1' contains the value 'value1'.
Traditionally, we need to check if the value is equal to test value, then we can operate on it. 
With the walrus operator, the value check can be done in one line.
If the value associated with the key needs to be checked as well, use parenthesis around the assignment expression.
Otherwise, the value being assigned will be the boolean expression and not the result of getting the key.  

test_value = 'value1'

# Traditional way
if my_dict.get('key1') == test_value:
    value = my_dict['key1']
    print(value)

# Walrus Operator
if (value := my_dict.get('key1')) == test_value:
    print(value)

#### Reading Streams
A stream, such as a file, may need to be read n bytes at a time without knowing the full length.
This can be accomplished with a while loop, but it's much simpler with the walrus operator. 
Let's open our file, and try to accomplish this traditionally. 
This file has some number of bytes of text on a single line.
We assign the first chunk to red_bytes, then we start our while loop.
At the end of our while looop we grab the next chunk, and when we run out of bytes the loop stops. 

def process_bytes(b):
    print(b)

# Traditional Way
my_file = open('my_file.txt', 'rb')

read_bytes = my_file.read(10)
while read_bytes: 
    process_bytes(read_bytes)
    read_bytes = my_file.read(10)

my_file.close()

With the walrus operator, the read step can be on the same line as the while loop, 
and there is no need for another my_file.read call inside the while loop.

# Walrus Operator
my_file = open('my_file.txt')

# Much simpler and easier to understand
while read_bytes := my_file.read(10): 
    process_bytes(read_bytes)

my_file.close()


# Thanks for Watching
Thanks for watching this episode on the walrus operator.
The walrus operator can make a lot of code easier to write. 
Keep it in mind when you're writing something new or going back and refactoring.  
Be sure that you are using Python 3.8, as it's not valid in previous versions. 
Links to my blog post on the walrus operator and the video code are in the description. 
I'll see everyone next time. 

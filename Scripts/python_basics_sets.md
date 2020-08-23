
LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-basics-sets.html
Code: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Basics/Sets.py
Python Documentation: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

# Intro
Hi Everyone, SearingFrost here with another Python basics video.
Today we're going to talk about SETS.
Sets in Python are **unordered** collections of objects. 
They are very similar to mathematical sets especially in that there are no repeat objects and set operations like union and intersection are implemented. 
One of the best use of sets is to remove duplicates from other collections by turning them into sets. 
The simple set operations can also be very helpful, but if you need something more complex look into [pandas](https://pandas.pydata.org/). 
Frozen Sets are just sets that cannot be modified once they are created. 
This is useful when you want to guarantee immutability. 

### Creating Sets
Sets can be created in two ways, with curly brackets or the built in set function. 
Using curly brackets {}, you separate objects with commas
The builtin **set** function will create a set out of an iterable object. 

{1, 2, 3, 'a', 'b', 'c'}

my_list = [1, 2, 3, 'a', 'b', 'c']
my_set = set(my_list)

### Common Operations
**SCREENSHOT A LIST HERE**
All the basic operations for collections in Python work on sets. 
**len(set)**, **x in set**, **x not in set** work just like lists or other collections.
Adding to sets can be done with the **add(elem)** method or the **update(*other_sets*)** method.
Removing objects can be done with the **remove(elem)** method, the **discard(elem)** method, the **pop()** method, or the **clear()** method.
Let's create some sample sets...one of ints...one of strings...and one with an int and a string
The length of our int set is 3
And using the in operator we see that 1 is an element of it
Let's add a 4 with the add method
Let's add the elements of the mixed set with the update method.
Notice that 1 is a common element between them, but it only appears once because sets contain no duplicates.
We can remove specific elements with remove
Let's remove the element 4
If we try to remove an element that's not there, such as 4 again, we get a key error
Discard works just like remove, but it does not raise a key error if the element is missing
The pop method removes a random element and returns it.

set_ints = {1, 2, 3}
set_strings = {'hello', 'searing', 'frost'}
mixed_set = {1, 'hello'}

len(set_ints)

1 in set_ints

set_ints.add(4)
set_ints

set_ints.update(mixed_set)
set_ints

set_ints.remove(4)
set_ints
set_ints.remove(4)

set_ints.discard(4)
set_ints

set_ints.pop()
set_ints

### Set Operations
**SCREENSHOT LIST**
Python also defines set specific operations.
* Union: **|** operator, returns all elements from 2 sets. Like a SQL full outer join.
* Intersetsion: **&** operator, returns common elements from 2 sets. Like a SQL inner join.
* Difference: **-** operator, returns elements from first set that aren't in the second set. Like a SQL left only join.
* Symmetric Difference: **^** operator, returns elements in 1 set but not both. Like SQL full outer join minus an inner join.

The union of set ints and set strings is all 6 elements
The intersection of set ints and set strings is the empty set, because they contain no elements in common
If we intersect set strings and mixed set we get the set containing just 'hello'
The difference of set strings minus set ints is just the set of strings
But if we take the differece of set strings minus the mixed set, we lose the common element 'hello'
Symmetric Difference for set strings and set ints is all the members of both sets
But the symmetric difference of set strings and the mixed set drops hello because it's in the intersection of the 2 sets.

set_ints = {1, 2, 3}
set_strings = {'hello', 'searing', 'frost'}
mixed_set = {1, 'hello'}

# Union
set_ints | set_strings


# Intersection
set_ints & set_strings

set_strings & mixed_set

# Difference
set_strings - set_ints

set_strings - mixed_set

# Symmetric Difference
set_string ^ set_ints

set_strings ^ mixed_set


# Thanks for Watching
Thanks for watching this python basics video on sets. 
They are very useful for some quick and dirty joins or dedups, use them as needed. 
Links to my blog post on sets and the video code are in the description. 
I'll see everyone next time. 

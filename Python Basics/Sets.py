# Creating Sets
{1, 2, 3, 'a', 'b', 'c'}

my_list = [1, 2, 3, 'a', 'b', 'c']
my_set = set(my_list)


# Common Operations
set_ints = {1, 2, 3}
set_strings = {'hello', 'searing', 'frost'}
mixed_set = {1, 'hello'}

# len
print(len(set_ints))
# 3

# in operator
print(1 in set_ints)
# True

# add(elem) method
set_ints.add(4)
print(set_ints)
# {1, 2, 3, 4}

# update(other_sets)
set_ints.update(mixed_set)
print(set_ints)
# {1, 2, 3, 4, 'hello'}

# remove(elem)
set_ints.remove(4)
print(set_ints)
# {1, 2, 3, 'hello'}
# KeyError if we try to remove(4) again
set_ints.remove(4)
# KeyError: 4

# discard(elem)
# Works the same as remove, but does not raise KeyError if element not in set
set_ints.discard(4)
# No KeyError
print(set_ints)
{1, 2, 3, 'hello'}

# pop()
# Just remove an element and returns it
print(set_ints.pop())
# 1
print(set_ints)
# {2, 3, 'hello'}


# Set Operations
set_ints = {1, 2, 3}
set_strings = {'hello', 'searing', 'frost'}
mixed_set = {1, 'hello'}

# Union
print(set_ints | set_strings)
# {1, 2, 3, 'frost', 'hello', 'searing'}

print(set_ints | mixed_set)
# {1, 2, 3, 'hello'} 
# Notice 1 is only present a single time, because sets don't contain duplicates

# Intersection
print(set_ints & set_strings)
# set()
# Empty set

print(set_strings & mixed_set)
# {'hello'}
# 'hello' is the only common element

# Difference
print(set_strings - set_ints)
# {'frost', 'hello', 'searing'}
# Everything returned, notice order is not preserved

print(set_strings - mixed_set)
# {'frost', 'searing'}
# 'hello' excluded because it's a memeber of mixed_set

# Symmetric Difference
print(set_string ^ set_ints)
# {1, 2, 3, 'frost', 'hello', 'searing'}
# Every member in new set

print(set_strings ^ mixed_set)
# {1, 'frost', 'searing'}
# Only members in 1 set but not both, 'hello' exluded

print(set_ints ^ mixed_set)
# {2, 3, 'hello'}
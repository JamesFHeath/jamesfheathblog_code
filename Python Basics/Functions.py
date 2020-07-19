def my_function(arg1, arg2):
    return arg1 + arg2

def my_function(arg1, arg2):
    return arg1 + arg2

return_value = my_function(1, 1)
print(return_value)
# 2

### Default Parameters
def my_function(arg1=1, arg2=2):
    return arg1 + arg2

# Calling my_function using defaults
return_value = my_function()
print(return_value)
# 3

# Calling my_function overwriting defaults
return_value = my_function(4, 5)
print(return_value)
# 9

def my_list_mutator(arg_list, arg_function):
    new_list = []
    for arg in arg_list:
        # Function is applied to the items in the list and appended to the new list that is returned
        new_list.append(arg_function(arg))
    return new_list

def my_double_function(x):
    return x * 2

# Passing in my_double_function without parentheses so it's not evaluated
doubled = my_list_mutator([1, 2, 3], my_double_function)
print(doubled)
# 2, 4, 6

# This lambda function will take an argument, double it, and return the new value
(lambda x: x * 2)
print((lambda x: x * 2)(5))
# 10

# Going back to our list doubling example, it's much nicer with a list comprehension and lambda
doubled = [(lambda x: x * 2) for x in [1, 2, 3]]
print(doubled)
# 2, 4, 6

# This can be made more compact with some syntatic sugar for list comprehensions
doubled = [x * 2 for x in [1, 2, 3]]
print(doubled)
# 2, 4, 6
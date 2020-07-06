# x is a list of length 3, with two ints and a string
x = [1, 2, 'hello']
# y is a list of length 0, the empty list
y = []

# z_error will generate a syntax error, because two integers and a string are not an iterable
z_error = list(1, 2, 'hello')

# Iterables can be any sequence that implements iterable
z_from_x = list(x)
z_from_brackets = list([1, 2, 'hello'])

# Even range will work!
z_from_range = list(range(10))


# Empty list can be created too
z_from_y = list(y)
z_from_no_args = list()

# Here we take the numbers 0..9 from range(10) and square them to get a new list
zero_to_nine_squared = [x**2 for x in range(10)]


# We can use any function in place of the exponential function, this function just ignores x and returns all 1s
ten_ones = [(lambda x : 1)(x) for x in range(10)]

index_list = [1, 2, 3, 4, 5]
# First value is 1
value_of_one = index_list[0]
# A slice can be a bit confusing, 1 refers to 2, and it creates a slice up to but not including index 4.
# One way of remember this is to start at the first value, and generate a list of 4 -1 = 3
list_from_2_to_4 = index_list[1:4]


mutate_by_index = [1, 2, 3, 4, 5]
mutate_by_index[0] = 77


append_list = [1, 2, 3]
append_list.append(4)
append_list.extend([5, 6, 7])

my_list = [1, 7, 'goodbye']
len(my_list)


search_value = 'SearingFrost'
search_value in ['SearingFrost', 'NotSearingFrost', 1, 2, 3]


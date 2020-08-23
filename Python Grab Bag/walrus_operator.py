my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Traditional way
if 'key1' in my_dict:
    value = my_dict['key1']
    print(value)
    # do some work with value...

# Walrus Operator
# get returns None if the value is not found
if value := my_dict.get('key1'):
    print(value)
    # do some work with value...

test_value = 'value1'

# Traditional way
if my_dict.get('key1') == test_value:
    value = my_dict['key1']
    print(value)
    # do some work with value...

# Walrus Operator
if (value := my_dict.get('key1')) == test_value:
    print(value)
    # do some work with value...
def process_bytes(b):
    print(b)

# Traditional Way
my_file = open('my_file.txt')

read_bytes = my_file.read(10)
while read_bytes: 
    process_bytes(read_bytes)
    read_bytes = my_file.read(10)

my_file.close()

# Walrus Operator
my_file = open('my_file.txt')

# Much simpler and easier to understand
while read_bytes := my_file.read(10): 
    process_bytes(read_bytes)

my_file.close()
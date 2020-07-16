# Creating Tuples with parentheses
t = (1, 2, 3, 'hello')

# Creating Tuples with tuple function
l = [1, 2, 3]
t = tuple(l)

# Accessing Tuples
t = ('a', 'b', 'c')
t[0]
t[1]

for item in t:
    print(item)

# t[0] = 'banana' ERROR


# Tuple Unpacking
t = ('a', 'b', 'c')
x, y, x = t


def dummy_server_call():
    return (200, 'success')

code, message = dummy_server_call()

# Named Tuples
from collections import namedtuple

HttpResponse = namedtuple('HttpResponse', ['code', 'message'])

def dummy_server_call():
    return HttpResponse(200, 'success')

response = dummy_server_call()
response.code
response.message
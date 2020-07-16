# Creating Strings with String Literals
s = 'hello'
s2 = "hello"
s3 = '''hello'''
s4 = """hello"""

# Creating Strings with str function
int_five = 5
str_five = str(5)
str_five

d = {'key': 55}
str_d = str(d)
str_d

# Accessing Elements
s = 'hello'
s[0]

# s[4] = 't' ERROR

s[0:2]

# Concatenation
s1 = 'hello '
s2 = 'world'
s3 = s1 + s2

# Replace and Split
s1 = 'SearingFrost'
s2 = s1.replace('Frost', 'Fire')

s1 = 'Searing, Frost, Fire'
l = s1.split(',')

# String Formatting with f strings
sf = 'Searing Frost'
f_string = f'Hello, my name is: {sf}'

expression_string = f'1 + 1 = {1 + 1}'
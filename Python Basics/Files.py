with open('my_file.txt') as my_file:
    # We create the my_file object and operate on it in this indented block
    file_contents = my_file.read()

print(file_contents)
with open('my_file.txt') as my_file:
    # my_file.read() will read all the contents of the file and assing it to the variable file_contents
    file_contents = my_file.read()

with open('my_file.txt') as my_file:
    # We can also iterate line by line with a for loop
    for line in my_file:
        print(line)
    # This will print each line of the file


with open('my_file.txt', mode='w') as my_file:
    my_file.write('SearingFrost')

with open('my_file.txt') as my_file:
    searing_frost = my_file.read()

print(searing_frost)
# SearingFrost

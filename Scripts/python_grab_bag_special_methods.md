LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-grab-bag-special-methods.html
Code: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Grab%20Bag/special_methods.py
Python Documentation: https://docs.python.org/3/reference/datamodel.html#specialnames

# Intro
Hi Everyone, SearingFrost here. 
Today we're going to reach into the Python grab bag and pull out special methods.

Special Methods in Python, also known as magic methods or dunders, are methods that allow Python operators to work on objects. 
Special methods start and end with double underscores, thus the name dunders. 
For example, objects that have a __len__ method can have the builtin len() function called on them; 
Objects that have the __iter__ method can be used in iteration with for i in object. 
We're going to go over a couple of implementations, but the options are basically limitless. 

# Addition with Animal Objects
The addition operator can be used on custom objects. 
Let's implement a cat class, and when we add a male cat and female cat with the plus operator we should get a kitten. 
Our cat class will be simple, and just have a gender. 
Let's put in the __add__ method, that takes another cat.
If the cat's genders are opposite, then we will return a kitten, and just give them the gender of the first cat.
We can then create a male cat...and a female cat
And when we use the + operator we get a kitten!

class Cat():
    def __init__(self, gender):
        self.gender = gender
    
    def __add__(self, other):
        if self.gender != other.gender:
            return Kitten(self.gender)
        else:
            return None

class Kitten(Cat):
    def __init__(self, gender):
        super(gender)

male_cat = Cat('male')
female_cat = Cat('female')

print(male_cat + female_cat)
# <__main__.Kitten object at 0x7fb92d738a90>


# Iteration over a Tree
Trees are data structures that can be accessed in a variety of ways. 
Let's implement a binary tree, which is a tree with a root and two nodes that are either empty, or another binary tree. 
I'm going to just sticking to integers for simplicity
Each tree will have a value, and then a left and right node

**Screenshot**
class IntegerBinaryTree():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left 
        self.right = right

To iterate through this binary tree, it requires its own __iter__ and an additional BinaryTreeIterator class that implements __iter__ and __next__.
**Screenshot some specification  text here**

Using the **for i in object** syntax, Python will call the iterator's __next__ method until a **StopIteration** exception is raised. 
When IntegerBinaryTree's __iter__ method is called, it needs to return an instance of **BinaryTreeIterator**.
BinaryTreeIterator will iterate through instances of IntegerBinaryTree **depth first**, though many implementations are possible. 
Depth first will require a stack, while breadth first requires a queue. 
The details aren't too important here, I just implemented this search algorithm from scratch so it's probably not optimal. 
The important parts are the stack which will keep track of what nodes have been visited, and the raising of StopIteration when all values have been exhausted.

We just need to add the __iter__ method on our IntegerBinaryTree and have it return an instance of BinaryTreeIterator

Now that the iter method is defined, it can be tested with a binary tree.
I've made it so the integers values are also the order of depth first traversal. 
And this is the equivalent tree in Python.
And now we can iterate through the tree using for value in root, and print out the values in the correct order. 

**Screenshot**
class BinaryTreeIterator():
    def __init__(self, b_tree):
        self.stack = []
        self.current = b_tree
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        value = self.current.value
        
        if (left := self.current.left) is not None:
            self.stack.append(self.current)
            self.current = left
        elif (right := self.current.right) is not None:
            self.current = right
        else:
            while True:
                try:
                    if (right := self.stack.pop().right) is not None:
                        self.current = right
                        break
                except IndexError:
                    self.current = None
                    break
            
        return value
        
class IntegerBinaryTree():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
    def __iter__(self):
        return BinaryTreeIterator(self)

**Add binary tree ascii**

eleven = IntegerBinaryTree(11, None, None)
ten = IntegerBinaryTree(10, None, None)
nine = IntegerBinaryTree(9, ten, eleven)
eight = IntegerBinaryTree(8, None, None)
seven = IntegerBinaryTree(7, None, eight)
six = IntegerBinaryTree(6, seven, nine)
five = IntegerBinaryTree(5, None, None)
four = IntegerBinaryTree(4, five, None)
three = IntegerBinaryTree(3, None, None)
two = IntegerBinaryTree(2, three, four)
root = IntegerBinaryTree(1, two, six)

for value in root:
    print(value)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11

# Thanks for Watching
Thanks for watching this grab bag episode on special methods. 
Customizing your classes to use standard Python syntax is a fantastic way to increase usability and help new users jump in and start working with your code. 
It's also just a lot of fun!
Links to my blog post on special methods and the video code are in the description. 
I'll see everyone next time. 
# Add method
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

# Iterator with a binary tree depth first traversal
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
# Basic Class
class MyClass:
    pass

# Attributes
class TwoAttrClass:
    x = 'Two Attribute Class Variable'
    def f(self):
        return 'Two Attribute Class Function'

TwoAttrClass.x
TwoAttrClass.f()

TwoAttrClass.y = 'Extra Attribute'
TwoAttrClass.y

class MyClass:
    pass

my_object = MyClass()
my_object

# __init__
class InitClass:
    x = 1
    y = 2
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

init_object = InitClass(x=3, y=4, z=5)

init_object.x
init_object.y
init_object.z

InitClass.x
InitClass.y
InitClass.z

# Methods
class ClassWithMethod:
    def my_method(self):
        return f'method called with object: {self}'

object_with_method = ClassWithMethod()
object_with_method.my_method
object_with_method.my_method()

ClassWithMethod.my_method(object_with_method)

# Inheritance
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

# isinstance
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

d = DerivedClass()
isinstance(d, DerivedClass)
isinstance(d, BaseClass)

# issubclass
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

issubclass(DerivedClass, BaseClass)

# Derived Attributes and Methods
class BaseClass:
    base_attribute = 'base attribute value'

    def __init__(self, x):
        self.x = x    

class DerivedClass(BaseClass):
    def __init__(self, x, y):
        # Call to BaseClass __init__
        super().__init__(x)
        self.y = y

derived_object = DerivedClass(x=1, y=2)

derived_object.x
derived_object.y
derived_object.base_attribute

class BaseClass:
    def __init__(self, x):
        self.x = x    

class DerivedClass(BaseClass):
    def __init__(self, x, y):
        self.x = x    
        self.y = y

derived_object = DerivedClass(x=1, y=2)

derived_object.x
derived_object.y
derived_object.base_attribute

# Multiple Inheritance
class BaseClassA:
    pass

class BaseClassB:
    pass

class DerivedClassAB(BaseClassA, BaseClassB):
    pass

# Private Fields
class PrivateClass:
  _x = 'private by convention'

# Static methods
class StaticMethodClass:
    @staticmethod
    def f():
        return 'I belong to the class'

StaticClassMethod.f

o = StaticMethodClass()
o.f
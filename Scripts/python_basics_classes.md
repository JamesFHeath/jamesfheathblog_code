Link:
https://blog.jamesfheath.com/2020/07/python-basics-classes-and-objects.html
Python Classes: https://docs.python.org/3/tutorial/classes.html
Multiple Inheritance: https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
Method Resolution Order: https://www.python.org/download/releases/2.3/mro/

# Introduction
Hi Everyone, SearingFrost here with another Python Basics Video.
Today, we'll be talking about classes, objects, and object oriented programming in Python.
Python is an object-oriented languge with all the standard class features like inheritance, instantition, and methods. 
Python defines classes in a flexible and simple way. 
Unlike Java/C++, all class members are public and class definitions are easily mutated at runtime. 
This video assumes some familiarity with object oriented concepts, and I'll also give some examples in Java as well to illustrate Python differences. 

# Defining a Class
Classes are defined with the **class** keyword. 
Any named statements will be added as attribute to the class. 
Defining variables and functions is conventional, but any statement is allowed. 
Class attributes can be accessed with dot syntax.
Additional attributes can be added at any time with dot syntax as well.

Let's define the simplest class possible, MyClass. 
It does nothing, the pass keyword exists to say "do nothing". 

Let's define a more interesting class, and give it two attributes. 
x is a string, and f is a function. 
We'll come back to the self parameter soon. 

Accessing x and f are done with dot notation. 
Adding the attribute y just requires an assignment, then y is part of the class. 
Python gives the programmer complete and easy access to change classes at runtime. 
Whether you want to be doing this a lot is another question. 

class MyClass:
    pass

class TwoAttrClass:
    x = 'Two Attribute Class Variable'
    # We will come back to the self parameter soon
    def f(self):
        return 'Two Attribute Class Function'

TwoAttrClass.x
TwoAttrClass.f()

TwoAttrClass.y = 'Extra Attribute'
TwoAttrClass.y

# Objects
Objects can be created by calling a class name just like a function, with parentheses. 
Let's go back to MyClass. 
We can define my_object and it is an instance of MyClass
In Java and many other languages, you create objects with the new keyword
my_object isn't very interesting, so let's see if we can do more with an init method. 

class MyClass:
    pass

my_object = MyClass()
my_object

MyClass myJavaObject = new MyClass();

**Screenshot here for init**
To perform setup on a newly created object, we can define an init method inside the class definition. 
Init methods are Python's equivalent to Java constructors.
When a class with an init function is instantiated, the init method is automatically called with the parameters passed in. 
Let's define a class named InitCLass with two attribute x and y, and an init method. 
The first parameter to the init method is self, which will refer to the instance of the object being created. 
Self is just a naming convention, any name is acceptable. 
Our init also takes 3 parameters, x y and z
We can instantiate this object py passing in the paremters for x, y and z. 
The self parameter is passed in automatically. 
We've now created an object that has the attributes x, with value 3...y, with value 4...and z, with value 5.
We can also see that the values for x and y for InitClass are still 1 and 2, they haven't been changed. 
If we try to access the attribute z on InitClass, we get an error because z only belongs to the object init_object.  

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
Methods are functions that are attached to object instances. 
Init is a special example of a method, but you can define your own methods to give more functionality to your objects.
Just like init, the first parameter of a method, self, is the object instance.
Here we create a class with a single method, and we'll have it return a string and the contents of self. 
Then we can create an instance of ClassWithMethod.
When we check my_method on the object, we can see it is a bound method.
Remember, calling the method passes in self automatically, so we don't need to pass any parameters explicitly. 
This call is equivalent to calling the class's method and passing in the object as a parameter

class ClassWithMethod:
    def my_method(self):
        return f'method called with object: {self}'

object_with_method = ClassWithMethod()
object_with_method.my_method
object_with_method.my_method()
ClassWithMethod.my_method(object_with_method)

Java hides the **this** parameter, the object instance just like self, within constructors and method signatures. 
Here's a basic java class, I've commented out the parameter this illustrative purposes. 
Another difference is that Java also requires the fields to be declared in the class definition.
Python fields can be added dynamically to classes and objects. 
public class MyClass{
    int x;
    int y;

    public MyClass(*this*, x, y) {
        this.x = x;
        this.y = y;
    }
}


# Inheritance
Inheritance is used to create a derived class with the properties of its base or parent class. 
In Python, inherited classes are added to the class signature. 
DerivedClass inherits from BaseClass

class BaseClass:
    pass

class DerivedClass(BaseClass)
    pass
 
Use **isinstance(object, class)** to check if an object is an instance of class or if class is one of its ancestors. 

class BaseClass:
    pass

class DerivedClass(BaseClass)
    pass

d = DerivedClass()
isinstance(d, DerivedClass)
isinstance(d, BaseClass)

Class inheritance can also be checked with **issubclass(derived_class, base_class)**. 

class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

issubclass(DerivedClass, BaseClass)

Derived classes receive all the attributes of their base class. 
Any attribute can be overwritten by the derived class with no restrictions. 
Attributes are first searched for in the derived class, and then to the bases class and so on. 
Use **super** to explicitly call the base class. 
Override __init__ from BaseClass

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
Python also supports multiple inheritance. 
Let's define baseclassa
And baseclassb
Then we can created DeriveClassAB with the base classes separated by commas
Multiple inheritance can have some gotchas, because there are multiple ways to search for base class attributes. 
Python uses a left to right, depth first search based algorithm to search the class hierarchy. 
I've linked the documentation in the video description. 
https://www.python.org/download/releases/2.3/mro/

class BaseClassA:
    pass

class BaseClassB:
    pass

class DerivedClassAB(BaseClassA, BaseClassB):
    pass

# Private Fields
Java and other languages have private fields and methods that can only be accessed from inside the class. 
Python on the other hand has no restrictions on access. 
If you don't want a client using a field or method you should prefix its name with an underscore. 
This isn't enforced by the language, but is a convention that most Python programmers understand. 
Here we can create a class that has an attribute underscore x, enforced by convention.
And the java equivalent is just the variable x with the private keyword in front of it. 

class PrivateClass:
  _x = 'private by convention'

class JavaPrivateClass {
    private x = 'private enforced by language';
}

# Static Methods
Static methods are methods that belong to the class but not any specific object instantiation. 
Python uses the **@staticmethod** decorator to define a static method, 
In Java, the equivalent is the static keyword.  
TwoAttrClass contains 2 attributes, the variable x and the function f
notice no self parameter for the static method 
When we create an object instance, and check the static function, it's accessible but we can see its type is function and not bound method like we saw before. 

class StaticMethodClass:
    @staticmethod
    def f():
        return 'I belong to the class'

StaticClassMethod.f

o = StaticMethodClass()
o.f

# Thanks for Watching
Thanks for watching this introduction to Classes and Objects in Python. 
Python is an object oriented programming language when you want, and is flexible enough to be a straightforward imperitave language or even functional language. 
If you're moving from Java or C++, just be mindful of the dynamic nature of Python. 
If you've been happily using Python without classes, being aware of them is important for reading code, but continue to write Python in whatever style you prefer. 
Flexibility is the beauty of Python. 
Links to the code and my blog post on classes and objects are in the description. 
I'll see everyone next time. 
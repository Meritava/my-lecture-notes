#INHERITANCE
"""
the class that inherits is called the sub class while the class we inherits from is called the super class
Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.
dir returns a list of attributes
"""
class Animal():         #this is the parent class
    pass

    class Birds(Animal):      #it inherits all the attributes from the animal class
        pass
"""
Module: geometry_classes

This module defines base and derived geometric classes for calculations and validations.

Classes:
- BaseGeometry: A base class for geometric calculations.

Module Author:
Merit

Last Updated:
24/08/2023

"""
class aMetaClass(type):
    """
    this is a metaclass that is created so that any class that is created inherits the method of this class. hey type is a class that every class created in python inherites from
    """
    def __dir__(cls):
        """
        this is to remove the init subclass
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']

class BaseGeometry:
    """
    A base class for geometric calculations.

    """
    def __dir__(cls):
        """
        this is to remove the init subclass
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']
    
bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))


























"""
Module: geometry_classes

This module defines base and derived geometric classes for calculations and validations.

Classes:
- BaseGeometry: A base class for geometric calculations.

Module Author:
Merit

Last Updated:
24/08/2023

"""
class aMetaClass(type):
    """
    this is a metaclass that is created so that any class that is created inherits the method of this class. hey type is a class that every class created in python inherites from
    """
    def __dir__(cls):
        """
        this is to remove the init subclass
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']

class BaseGeometry:
    """
    A base class for geometric calculations.

    """
    def __dir__(cls):
        """
        this is to remove the init subclass
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']
    def area(self):
        """
        Calculate the area of a geometric shape. Not implemented in the base class.

        Raises:
        Exception: Indicates that area calculation is not implemented.
        """
        raise Exception ("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Methods:
    - __init__(width, height): Initialize a Rectangle instance with width and height.
    - area(): Calculate the area of the rectangle.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("must be an integer")
        if width <= 0:
            raise ValueError("must be greater than 0")
        if not isinstance(height, int):
            raise TypeError("must be an integer")
        if height <= 0:
            raise ValueError("must be greater than 0")
        

















"""
Module: rectangle.py
This module defines the Rectangle class, which inherits from the Base class.
"""
from models.base import Base
class Rectangle(Base):
    """
    Represents a rectangle, a subclass of the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The unique identifier of the rectangle.
        """
        super().__init__(id)
        self.__width = width
        __height = height
        __x = x
        __y = y

    @property
    def width(self):
            """
        Getter for the width attribute.
        """
            return self.__width
    @width.setter
    def width(self, value):   #This is the definition of the setter method for the width attribute. The self parameter refers to the instance of the class, and the value parameter is the new value you want to assign to the width attribute
            """
        Setter for the width attribute.
        """
            self.validate_positive_integer(value, 'width')
            self.__width = value
    @property
    def height(self):
            """
            Getter for the height attribute.
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter for the height attribute.
            """
            self.validate_positive_integer(value, 'height')
            self.__height = value

        @property
        def x(self):
            """
            Getter for the x attribute.
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            Setter for the x attribute.
            """
            self.validate_non_negative_integer(value, 'x')
            self.__x = value

        @property
        def y(self):
            """
            Getter for the y attribute.
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            Setter for the y attribute.
            """
            self.validate_non_negative_integer(value, 'y')
            self.__y = value
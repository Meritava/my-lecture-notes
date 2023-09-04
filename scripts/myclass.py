#create a class
#note attribute is same as variable and function is same as method in object programming language
class MyClassName:
    pass

# attributes of animals
    
    eyes = "eye"

#instance attribute... these attribute are specific to some particular animals
    color = "red"
    height = 12
    name = "name of animal"
#class attribute - these attributes are general
    biological_class = "annimalia"


class iphone14:
    height = "140cm"

    #attribute
    """
    - color
    - height
    - width
    - screen size
    - battery capacity
    - camera spec
    - sim avalaility

     #class attribute - apply to all the iphone14 to be produced
     #instance attribute - may defer based on the specific iphone14 produced
    """  
    """
    #methods - what are the functionality we want our iphone14 to have
    - allow game
    - video recording
    - messaging
    - calling
    - gps tracking

# to create an instance of a class - creating the object .... as soon as the object is created assign all these functionality and attribute to the object
    the self - anytime you want to create an object from the class, you call that object self
    """
    #dunder init method - for each copy that we create we can give it a color
    def __init__(self, mychoosencolor):
        self.color = mychoosencolor

    def makeCall(self):
        return("I am calling someone")    #this is a functionality, that would be define in our iphone14, so any time this function is called, it will execute

# how to instatiate an object of the class
daraPhone = iphone14("Red")
meritPhone = iphone14("Blue")

#checking id the iphone14 was created
print(daraPhone)
print(meritPhone)
#checking the color
print(daraPhone.color)
#checking the height
print(daraPhone.height)
#calling the method/function
print(daraPhone.makeCall())


"""
#NOTEE FROM RESOURCES
Object Oriented Programming
 A class creates a new type where objects are instances of the class. 
Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class.
Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields.
Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.
Collectively, the fields and methods can be referred to as the attributes of that class.
Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self
Say you have a class called MyClass and an instance of this class called myobject. When you call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) - this is all the special self is about.

#example:
class Person:
    pass  # An empty block

p = Person()
print(p)
output:
$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>
notte - The simplest class possible is shown in the following example (save as oop_simplestclass.py).
How It Works

We create a new class using the class statement and the name of the class. This is followed by an indented block of statements which form the body of the class. In this case, we have an empty block which is indicated using the pass statement.

Next, we create an object/instance of this class using the name of the class followed by a pair of parentheses. (We will learn more about instantiation in the next section). For our verification, we confirm the type of the variable by simply printing it. It tells us that we have an instance of the Person class in the __main__ module.

Methods
We have already discussed that classes/objects can have methods just like functions except that we have an extra self variable. We will now see an example (save as oop_method.py).
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()   #here is creating an instace of nthe class i.e. you creating an object from the class
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
Output:
$ python oop_method.py
Hello, how are you?

The __init__ method
The __init__ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object.
Example (save as oop_init.py):
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
Output:
$ python oop_init.py
Hello, my name is Swaroop
When creating new instance p, of the class Person, we do so by using the class name, followed by the arguments in the parentheses: p = Person('Swaroop').

We do not explicitly call the __init__ method. This is the special significance of this method.

Now, we are able to use the self.name field in our methods which is demonstrated in the say_hi method.



Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields.
The __init__ method:
The __init__ method is run as soon as an object of a class is instantiated (i.e. created).

class cordinate(object):  explaining this line of code;  class is that we are defining a class, cordinate is the class name.....objec is a parent class
def __init__(self, x, y)  explaining the line, __init__; is the name of the function..... def; we are starting with def because it is a function, x and y are parameters, like in function....the self is a parameter, it is the object itself, it is a placeholder for any sort of instance when you create the object, self is an instance of the object...self refers to a particular instance of the class
    self.x = x   explaining this line; whatsoever value of x that was passed into the object(self) that we are creating, we assign that value(x) to it
    self.y = y    explaining this line; whatsoever value of y that was passed into the object(self) that we are creating, we assign that value(y) to it
def distance(self, others): def, we are defining another function....distance iss the name of the function, self is an instance of the object....others is a parameter
x_diff_sq = (self.x - others.x)**2   #the dot notation is to access the value of x,first i want to access the x data of myself(i.e. the self.x), then subract that value from the x value of the other cordinate....you use the dot notation to determine whose data attribute you want to access...the other.x is the value in which we are finding the distance from, the point to our own point....you should always specify whose data attribute you want to access using the dot notation
def
y_diff_sq = (self.y - others.y)**2
return (x_diff_sq + y_diff_sq) ** 0.5
def __str__(self):
    return "<"+str(self.x)+","str(self.y)+">"
#now creating an object
c = cordinate(3, 5)  explaing this line, 3,5 is x and y.... c is self i.e. the object itself,....cordinate is the class name
zero = cordinate(0, 0)
print(c.distance(zero))   can also be written as print(coordinate.distance(c, zero)).....recall the method def distance(self, others)....so here, c is self and others is zero.. calling the distance function
print(c.x)  this will print the value of x in object c
print(isistance(c, coordinate))   #to find out if a particular object is an instance of a particular class, you use the isinstance of keyword


"""
print('hello world')
print("Merit")
# this is a single line comment
""""
this is a multi line commet
comment
you can also use single quotes
you can type cast that is change one data type to another using
int() changes to and int
float() changes to a float
complex data type are numbers with a letter j at the end
different data types
text type: string, strings are values stored in quotes
numeric type: int, float, complex... numeric data type are anything that is a number.. int is any whole number.. float is any number with a fractional part.. complex data type is any number with the letter j at the end
sequence type: list, tuple, range
mapping type: dictionary dict
set: set, frozenset
bollean: bool - true
none type: nonetype
"""
name = "Merit George"
age = 25
location = "Lagos"
print("my name is", name)
print(age)
print("i live in: " + location)
print("age " + str(age))

print(type(age))
float_value = float(age)

AGE = 10
HEIGHT = 12.5
IMAGINARY = 13j
NAME = "MERIT"
print("Hey " + NAME)
slice = NAME[0]
slice = NAME[-1] # it gives you the last character
slice = NAME[:4] # prints thhe first 4 charaacter
slice =     name[1:] # it omittes the first character
slice = NAME[2:4] # ommit the first 2 character and starts from the third one and ends at the third one. practice to see how it works
print(slice) #prints the first letter of NAME
# print(len(NAME))
# lets get same result as the commented line line 37
size = len(NAME)
slice = NAME[size - 1]
print(NAME + " " + "lenght of NAME" + str(size))
capital = NAME.lower()
print(capital)
rep = NAME.replace("M", "Li")
print(rep)
print("{} is my name {}".format(name, age))
print("{1} is my name {0}".format(name, age))   # it changes the position of the variable value, that is which variable should come first
isTrue = False  #boolean data type
print(5 > 10)
"""
operaors
arithemetic operators: +, -, *, %, /, **, //
assignment operator: =, +=
comparison operator: ==, <, >, <=, >=
logical operators: and, or, not
identity operator: is, is not
"""
"""
a program that ask the user to enter his/her name. and the program
should welcome the user with their name
if you want to get the laast digit of any number, you module(%) the number by 10 i.ei number % 10 = last number
"""
hername = input("please enter your name: ")
herage = input("please enter your age: ")
print("hello " + hername)
print("you are {} years old".format(herage))
# a program that ask the user for length and width and converts them to float numbers and multiplies them
length = float(input("enter length: "))
width = float(input("enter width: "))
area = length * width
print("the area of your room is {}".format(area))
#this is a list
c = ["hey","you",1,2,3,"go"]
print(c)
#tuple
a=(1,2,3,4)
print(a) #prints the whole tuple

#a sample dictionary variable
a = {1:"first name",2:"last name", "age":33}
#print value having key=1
print(a[1])
#print value having key=2
print(a[2])
#print value having key="age"
print(a["age"])
"""
using str.format example
Positional and keyword arguments used with string formatters give us more control over manipulating our original strings through reordering.
open_string = "Sammy loves {}."
print(open_string.format("open source"))
output - Sammy loves open source.

new_open_string = "Sammy loves {} {}."                      #{} 2 placeholders
print(new_open_string.format("open-source", "software"))    #Pass 2 strings into method, separated by a comma
Output
Sammy loves open-source software.

print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))
Output
Sammy the pilot fish has a pet shark!

print("Sammy the {0} {1} a {pr}.".format("shark", "made", pr = "pull request"))
Output
Sammy the shark made a pull request.

converting decimal to float
We will use the format code syntax {field_name:conversion}, where field_name specifies the index number of the argument to the str.format() method that we went through in the reordering section, and conversion refers to the conversion code of the data type that you are using with the formatter.
The conversion type refers to the the single-character type code that Python uses.
 The codes that we will be using here are s for string, d to display decimal integers (10-base), and f which we’ll use to display floats with decimal places
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
Output
Sammy ate 75.000000 percent of a pizza!
print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367))
Output
Sammy ate 75.765 percent of a pizza!
print("Sammy ate {0:d} percent of a pizza!".format(75.765367))
Output
ValueError: Unknown format code 'd' for object of type 'float'
print("Sammy ate {0:.0f} percent of a pizza!".format(75.765367))
Output
Sammy ate 76 percent of a pizza!
"""

"""
We can add a number to indicate field size (in terms of characters) after the colon : in the curly braces of our syntax:
print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))
Output
Sammy has    5 red balloons        !
In the example above, we gave the number 5 a character field size of 4, and the string balloons a character field size of 16 (because it is a long string).

As we see, by default strings are left-justified within the field, and numbers are right-justified. You can modify this by placing an alignment code following the colon. < will left-align the text in a field, ^ will center the text in the field, and > will right-align it.
Lets left-align the number and center the string:
print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))
Output
Sammy has 5    red     balloons    !

By default, when we make a field larger with formatters, Python will fill the field with whitespace characters. We can modify that to be a different character by specifying the character we want it to be directly following the colon:
print("{:*^20s}".format("Sammy"))
Output
*******Sammy********

We’re centering the string with ^, specifying that the field is 20 characters in size, and also indicating that we are working with a string conversion type by including s.
"""

"""
passing variables with the str.format()
nBalloons = 8
print("Sammy has {} balloons today!".format(nBalloons))
Output
Sammy has 8 balloons today!
sammy = "Sammy has {} balloons today!"
nBalloons = 8
print(sammy.format(nBalloons))
Output
Sammy has 8 balloons today!
"""

"""
Lets look at a typical for loop in Python that will print out i, i*i, and i*i*i in the range from 3 to 12:
for i in range(3,13):
    print(i, i*i, i*i*i)
    Output
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
11 121 1331
12 144 1728

for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
    Output
  3    9    27
  4   16    64
  5   25   125
  6   36   216
  7   49   343
  8   64   512
  9   81   729
 10  100  1000
 11  121  1331
 12  144  1728
 we accommodated for the size of each expected output, giving 2 extra character spaces for each, depending on the maximum possible number size, so our output looks like this: example above...We can specify a consistent field size number in order to have even columns, making sure that we accommodate the larger numbers.
 We can also manipulate the alignment of the columns by adding <, ^, and > for text alignment, change d to f to add decimal places, change field name index numbers, and more to ensure that we are displaying the data as we would like.
"""
"""
 x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
     x = 0
     print('Negative changed to zero')
 elif x == 0:
     print('Zero')
 elif x == 1:
     print('Single')
 else:
     print('More')
"""

"""
Ask user to input numbers - a comment split allows you to enter two data and split them
num1, num2 = input("enter 2 numbers ").split()    -code
Convert the string into regular integer - comment
num1 = int(num1)
num2 = int(num2)
sum the numbers and store in sum - comment
sum = num1 + num2
substarct value and store in difference - comment
difference = num1 - num2
print result - comment
print("{} + {} = {}".format(num1, num2, sum))
print("{} + {} = {}".format(num1, num2, difference))

age = eval(input("enter number: "))  the eval keyword allow you convert the input to an integer
if (age >= 1) and (age <= 18):
    print("important")
elif (age == 21) or (age == 50):
    print("important")
elif not(age < 65):
    print("important")
else:
    print("not important")
"""
"""
FOR LOOP
for i in[2, 4, 6, 8]:
    print("i = ", i)
    output:
    i = 2
    i = 4
    i = 6
    i = 8

for i range(10):
    print("i = ", i)
    output
    i = 0
    i = 1
    i = 2
    ...
    i = 9
for i range(2, 10):
    print("i = ", i)
    output
     i = 2
     i = 3
     i = 4
    ...
    i = 9

    to check if a value is odd or even
    i = 2
    print((i % 2) == 0)

for i range(1, 21):
    if((i % 2) != 0):
        print("i = ", i)

take a float and round it up to 2 decimal place
your_float = input("enter a float ")
your_float = float(your_float)
print("rounded to 2 decimal {:.2f}".format(your_float))
"""

"""
WHILE LOOP
import random #a library to import/input random number
rand_num = random.randrange(1,51) #takes random number between 1 and 51
i = 1
while (i != rand_num):
    i += 1
    print("the random value is: ", rand_num)

another example
i = 1
while (i <= 20):
    if (i % 2) == 0:
        i += 1
        continue #as long as i is <= 20 continue, do not print, increment and continue
        
        if i == 15:
            break # this will stop the loop when it gets to 15
        print("odd: ", i)
        i += 1
"""

#TUESDAY CLASS
"""
voting_limit = 18
height_limit = 6
age = int(input("are old are you: "))
height = int(input("what is your height: "))
if age >= voting_limit and height >= height_limit:
    print("you can vote")
elif age = voting_limit and height == height_limit:
    print("you are the perfect match to vote")
else:
    print("check back until you are 18+")

the not is use for a single statement

in python we have the while loop and the for loop
write a python program that counts from 0 to 10
example:
limit = 10
counter = 0
while counter < limit:
    print(counter)
        counter = counter + 1
else:
print ("loop ended")
example 2
limit = 10
counter = 0
while counter < limit:
    print("I love you") # i love you will be printed 10 times
        counter = counter + 1
else:
print ("loop ended")
example 3
limit = 10
counter = 0
name = "merit ishekwene"
while counter < size:
    print(name[counter].upper(), end="\n")
    counter = counter + 1

limit = 10
counter = 0
name = "merit ishekwene"
size = len(name)
while counter < size:
    print(name[counter].upper(), end="\n")
    counter = counter + 1
example 4
check for even numbers and odd numbers
limit = 20
counter = 1
while counter < limit:
    if counter % 2 == 0:
        print("{} is even".format(counter), end="\n")
    elif counter % 2 == 1:
        print("{} is odd".format(counter), end="\n")
    counter = counter + 1

FOR LOOP
numbers = range(10) #this is saying generate a range of ten numbers
for me in numbers:
    print(me)
    OR
    for number in range(10)
    print(number)
another example 
for number in range(10):
    if number % 2 == 0:
        print("lucky number {}".format(number))

    example:
for each_character in "merit":
print(each_character.upper(), end="")
membership operator: in, not in
identity operator: is, is not
example:
for number in range(100):
    print("{:02}".format(number), end=", ")
example:
for number in range(100):
    print("{:0x}".format(number), end=", ")
example:
for number in range(100):
    if number <= 50:
        print(number)
        break #the break keyword is use to stop the loop from continuing
        
example:
for number in range(99):
    if number <= 50:
        print(number)
        continue
else:
        print("loop ended")

    example:
for i in range(99):
    for j in range(99):
        print("{} * {} = {}".format(i, j, (i * j)))
"""

# Live learning session friday 21st july
"""
example one - defining a function and calling it
#! /usr/bin/python3
user_input = input("what is your name?")
def greetings(name):
    print("Hello {name}".format(name=name))

greetings(user_input)

example 2
#! /usr/bin/python3
user_input = input("what is your name?")
user_salary = float(input("What is your salary"))
def greetings(name, salary):
    print("function called", end="\n")
    print("Hello {name}".format(name=name))
    print("my salary {salary}".format(salary=salary))

greetings(user_input, user_salary)

ADDING TO EXAMPLE 2
#! /usr/bin/python3
BONUS_RATE = 0.3

user_input = input("what is your name?")
user_salary = float(input("What is your salary"))

def calculate_bonus(value):
    bonus = value * BONUS_RATE
    return bonus

def greetings(name, salary):
    print("function called", end="\n")
    print("Hello {name}".format(name=name)) #print("Hello")
    user_bonus = calculate_bonus(salary)
    print("The bonus calculated on your salary {} is {}".format(salary, user_bonus))
greetings(user_input, user_salary)
"""
"""
parameter is a container or a space/placeholder you are making available in your function, that holds the argument when the function is called.
The argument is the actual value you pass to the function parameter.
Whatever value/variable you define outside a function is a global variable while the variable/value you define inside a function is a local variable to that function.
HOW TO DEFINE A FUNCTION WHEN YOU DO NOT KNOW THE NUMBER OF ARGUMENT TO PASS IN
def greet_people(*people):
example:
def greet_people(*people):
    for persons in people:
        print("How do you do {}?".format(persons))

greet_people("merit", "mercy", "dami")

example:
def
"""

# Tuesday lecture 25th July 2023
# how to import files
"""
name of file 0-add, and it has some functions inside
import 0-add
from 0-add import sum #this two line of code imports the sum function from 0-add model/file
from 0-add import *  # this line import every function on the file 0-add
Always import the specific function you are asked to import
example: a function to add two numbers
def sum(a, b):
    return a + b

print(sum(2, 5))

DATA STRUCTURES
1. List
2. Tuple

print(list_2[2]) #this prints the third element on list_2
"""



# temp_value = float(input("input your temp value "))
# def converting(value):
#     converted_value = (5 / 9) * (value - 32)
#     return converted_value

# def convert_to_celsius(fahrenheit):
#     user_value = converting(fahrenheit)
#     print("Your temp is {}".format(user_value))

# convert_to_celsius(temp_value)



# for i in range(100):
#     print("{:02d}".format(i),end=", ")
#     if i < 99:
#         print(end="\n")


#PYTHON IMPORT MODULE
"""
If you intend to use a function often you can assign it to a local name:
>>> fib = fibo.fib
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 
note here, the name of the module file is fibo and it has a function inside fib

we can also import several function like this: from fibo import fib, fib2  .. seperating the function with a comma
to import all files: from fibo import *  ... note fibo is the module file name

Note For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use imp.reload(), e.g. import imp; imp.reload(modulename).
#Handling exception error:
try:
    aList = [1, 2, 3]
    print(aList[3])
 except indexError:  #you can also catch multiple errors: except (indexError, NameError)
    print("that index doesnt exist")
 except:
    print("an unknown error occured")

    example: how finally is used
    num1, num2 = input("enter two values for division ").split()
try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {}".format(num1, num2, quotient))
except ZeroDivisionError:
    print("you cant divide by zero")
else:
    print("you didnt rasie an exception")
finally:
    print("i execute no matter what")

example: how rasie is used

"""

"""
27TH LECTURE - PYTHON CLASSESS & OBJECTS, INHERITANCE
user-defined data structure
Class - a class is a blueprint in which we are going to base our development on... it should be able to allow us model anything we want to model in our programming
the class is the blueprint on which you build other object. you can use a class to build as many copies of object as you want
A class is a collection of attribute and behaviour
Object - it is the actual product created from a class
Istatiation - the process of creating an object from a class
4 principles of object oriented programming
1. Encapsulation - it allows us to create a container for our code and only the one you give access to that's the o people will get access to
2. Inheritance - we create instances that are able to inherit from the parent class...example:
animal class(attribute and behaviour)
dog class (this dog class can inherit some attribute and behaviour from the animal class)
breed of dogs class (it can inherit from the dog class)
3.Polymorphism - attribute and behaviour should be common aboung every element using the class... example, when writing a class for the animal, you can not incluse wing as attribute because not all animal have wing
but if you are creating a bird classes, you can include wing, because all bird have wings
4.Abstraction - all you care about is how it functions. example the print function, you dont see abstract, the function(print example) has  been abstract from you
"""

#DATA STRUCTURE LISTS 7 tuples
"""
squares = list(map(lambda x: x**2, range(10)))
or, equivalently:
squares = [x**2 for x in range(10)]

example:
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
or, equivalently:
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#LEARN TO PROGRAM VIDEO - LIST
onetoten = list(range(10))
randlist = ["string", 12.44 8]
onetoten = list(range(10))
examplelist = ["meeri", 2929.44, 4]
examplelist = onetoten + examplelist
print(examplelist[0])
print(len(examplelist))
first3 = examplelist[0:3]
for i in first3:
    print("{} : {}".format(first3.index(i), i))
print(first3[0] * 3)  #it prints the first element three times
print("whatyou" in first3) #check if whatyou is inside of first3 list, will return a true or false value
print(first3.index("whatyou"))  #to print the index if the string is found
print(first3.count(4)) #to check how many times 4 occurs
first3[0] = "merit"  #change the element in the string who's index is 0
first3.append("another")  #adds another to the list
"""
"""
#create a list of five random items between 1 to 9
import random
import math
numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))

for i in numList:
    print(i)

numList = []
numList.sort()  #sorts a list
numList.reverse()  #reverse sort
numList.insert
numList.insert(5, 10)  #means 10 should be insert to the 5th index
numList.remove(10)  #it removes the value 10
numList.pop(2)  #removes whatever is in the second index
"""
eventList = [i*2 for i in range(10)]  #i*2 is the operation to be performed on the list, the the for statement defines the list
for i in eventList:
    print(i)



"""
#Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary
if you want it sorted, just use sorted(d.keys())
example of a dictionary:
tel = {'jack': 4098, 'sape': 4139}
When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
note, in comparison operators, not has the highest priority and or the lowest. As always, parentheses can be used to express the desired composition
The comparison operators in and not in check whether a value occurs (does not occur) in a sequence. The operators is and is not compare whether two objects are really the same object; this only matters for mutable objects like lists
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False



#LAMBDA: is used when you do not want to create too many function
sum = lambda x, y: x + y   #the sum is the function, the first statement x, y are the two attributes asigned, then x + y is the operattion to be performed on the attributes.
print(sum(4, 5))   #calling the lambda sum function
another example:
can_vote = lambda age: True if age >= 18 else False
print(can_vote(16))  #calling the function and passing a value 16
example:
powerList = [lambda x: x ** 2,
            lambda x: x ** 2,
            lambda x: x ** 2]

for func in powerList:
    print(func(4))


The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name...they are just needed where they have been created
syntax:
lambda argument_list: expression

#The Map() function
 map() is a function which takes two arguments:
r = map(func, seq)
"""

"""
#Understanding Lambda function
lambda args1, args2,... :then followed by what ever you want to do with the arguments
lambda is use when you need a small function and do not want to put several function i your code
the -> str means we are returning a string
def random_func(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age: ", age)
    print("Weight: ", weight)

    return "My name is {} and I am {} years old. And I weigh {}".format(name, age, weight)

print(random_func(24, "Merit", 5.5))    #it will print the value as it appers here

example:
sum = lambda x, y: x + y
print(sum(2, 5))
can_vote = lambda age: True if age >= 18 else False
print(can_vote(19))
example:
powerList = [lambda x: x ** 2,
            lambda x: x ** 3,
            lambda x: x ** 4]

for func in powerList:
    print(func(4))

#storing lamda inside dictionaries
#MAP
map lets us execute a function on each item on a list
example:
ontoten = range(1, 11)
def dubn(num):
    return num * 2
print(list(map(dubn, ontoten)))   #we added the list to convert whatsoever the result of the map was into a list
using lambda, you can just pass in the function directly
print(list(map((lambda x: x * 2), ontoten)))
we can also perform calculation against multiple different list
aList = list(map((lambda x, y: x + y), [1, 3, 5], [3, 4, 4]))
print(aList)
#filter select item from a list based of a function
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
#find multiple of 9 in random 100 numbers within the range of 1 to 1000
import random
randList = list(random.randint(1, 1001) for i in range(100))  #first generate the list
print(list(filter((lambda x: x % 9 == 0), randList)))
#REDUCE reduce a lis and return a single result
from functools import reduce
#add up the values 
print(reduce((lambda x, y: x + y), range(1, 6)))
"""

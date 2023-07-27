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
text type: string
numeric type: int, float, complex
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
print("{1} is my name {0}".format(name, age))   # it changes the position of the variable value
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
"""
hername = input("please enter your name: ")
herage = input("please enter your age: ")
print("hello " + hername)
print("you are {} years old".format(herage))

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
open_string = "Sammy loves {}."
print(open_string.format("open source"))
output - Sammy loves open source.

new_open_string = "Sammy loves {} {}."                      {} placeholders
print(new_open_string.format("open-source", "software"))    Pass 2 strings into method, separated by a comma
Output
Sammy loves open-source software.

print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))
Output
Sammy the pilot fish has a pet shark!

print("Sammy the {0} {1} a {pr}.".format("shark", "made", pr = "pull request"))
Output
Sammy the shark made a pull request.

converting decimal to float
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
numbers = range(10)
for me in numbers:
    print(me)
    OR
    for me in range(10)
    print(me)
another example 
for number in range(10):
    if number % 2 == 0:
        print("lucky number {}".format(number))
for each_character in "merit":
print(character.upper(), end="")
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
"""
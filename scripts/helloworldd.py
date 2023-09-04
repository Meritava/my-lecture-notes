# LIVE LEARNING SESSION INTRODUCTION TO PYTHON
"""
print('hello world') # you can use single or double quotes
print(3)
A variable is a container for storing data. Variable names are case sensitive
name = "Merit" #name is a container/variable, Merit is stored in name
age = 25
print(3)
name = "Merit"
age = 25
flaot_value = float(age) #changing age variable value to a float, it is called type casting
print(flaot_value)
print("my name is ", name)
print("my name is " + name)
print(age)
print("age is " + str(age))
print("{}".format(name))
print(type(name))
print("I " + name + " by name")
print(len(name)) #it gives the length of the string
size = len(name)
print(size)
print(name.upper()) #it can also be stored in a variable and printed
lowercase = name.lower()
print(lowercase)
print("{}".format(name))
print(name[0]) #this prints the first charater in the name variable
print(name[-1]) #this gives you the last character
print(name[:]) #the scolon is the slice operator
print(name[:2]) #this prints the first two letters
print(name[2:]) #removes the first two characters in thr string
print(name[1:2])
You can also store true or false values
"""
print(3)
name = "Merit"
age = 25
isTrue = True #this stores a value boolean data type, True
print(type(isTrue))
"""
# a program that ask the user for length and width and converts them to float numbers and multiplies them
length = float(input("enter length: "))
width = float(input("enter width: ")) #whenever you accept input from your user, it is in string so you have to change the data type, here we changed to float data type
area = length * width
print("the area of your room is {}".format(area))
"""
# Tuesday lecture
"""
Booleans data type: True, False
Comparison operators: ==, >, <, <=, >=
Decision
the decision is based on the comparison operators
Logical operators: and, or, not
identity operators: is, is not
membership operators:
"""

"""
LEARN TO PROGRAM VIDEO
num1, num2 = input("enter your number ").split()  #split allows you enter two numbers
Example:
half of the code:
print("{} + {} = {}".format(num1, num2, num1+num2))  #the format perform addition to both num1 and num2 and place the value in thee last format str
example:
num1, operator, num2 = input('enter cal ').split()
num1 = int(num1)
num2 = int(num2)
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "*":
    print("{} + {} = {}".format(num1, num2, num1*num2))
else:
    print("operator not included")

    
EXAMPLE:

MORE CONTROL FLOW LOOP
Example:
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
example:
for i in range(5):
print(i) #this prints from 0 to 4
example:
range(5, 10)
   5 through 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70

example:
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
example:
list(range(5))
[0, 1, 2, 3, 4]
example: check for prime numbers
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
example:
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9


example: We can create a function that writes the Fibonacci series to an arbitrary boundary:
>>> def fib(n):    # write Fibonacci series up to n
...    Print a Fibonacci series up to n.
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
"""
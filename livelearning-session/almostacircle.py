#LIVE LEARNING SESSION 8TH AUGUST
#type json python package on google
"""
#Dictionary in python
key:value pairs
student = {'name': 'merit', 'age': 25, 'height': 5}
print(student['name'])
len(student)
JSON is different from a dictionary by the quotation that encloses it....
Jsn is a lite way/weigt of transferring data from a clien to a server or between clients, it provide a light/lite weight method of transferring data
import json
json.dumps(student)   #this converts the dictionary to a json file
"""
student = {'name': 'merit', 'age': 25, 'height': 5}
print(student['name'])
len(student)
import json
json.dumps(student)   #this converts the dictionary to a json file
stringified = json.dumps(student)
stringified
stringified['name']  #it will not print, so you have to convert back to object/dictionary before it can print
parsed = json.loads(stringified)   #converters back to dictionary/object
parsed
parsed['name']  #it works

"""
"""
#HTTP

"""
#RESOURCES ON ALMOST A CIRCLE PROJECT
it is not necessary to write *args or **kwargs. Only the * (aesteric) is necessary. You could have also written *var and **vars
*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a function. What does variable mean here is that you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords.
*args is used to send a non-keyworded variable length argument list to the function. Here’s an example to help you get a clear idea:
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')
OUTPUT:
first normal arg: yasoob
another arg through *argv : python
another arg through *argv : eggs
another arg through *argv : test

The * symbol in front of args is used to collect all additional positional arguments into a tuple.
Example:
def print_args(*args):
    for arg in args:
        print(arg)

print_args('apple', 'banana', 'cherry')
# Output: apple
#         banana
#         cherry

The **kwargs parameter in a function allows you to pass a variable number of keyword arguments to the function.
The ** symbol in front of kwargs is used to collect all additional keyword arguments into a dictionary.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_kwargs(fruit='apple', dessert='cake', drink='juice')
# Output: fruit apple
#         dessert cake
#         drink juice

def example_function(arg1, arg2, *args, kwarg1=None, kwarg2=None, **kwargs):
    print("Positional Arguments:", arg1, arg2)
    print("Additional Positional Arguments:", args)
    print("Keyword Arguments:", kwarg1, kwarg2)
    print("Additional Keyword Arguments:", kwargs)

example_function(1, 2, 'a', 'b', kwarg1='x', kwarg2='y', fruit='apple', drink='water')
In this example, arg1 and arg2 are mandatory positional arguments, *args collects additional positional arguments, kwarg1 and kwarg2 are optional keyword arguments, and **kwargs collects additional keyword arguments.

"""

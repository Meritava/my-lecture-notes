# function: grouping code block that are related to one another. i have a function that does this and a function that does that
# the def keyword is use in defining/creating a function with parenthesis and a colon
"""
def helloworld():
    pass - pass means you don't want to write anything in the function, you just want to define it
"""
#creating/defining a function
def helloworld():
    print("hello world biggest dream")
#call/invoke a function
helloworld()

def howdy(user):
    print("howdy {}".format(user))
howdy(user="merit") #howdy("merit") will work as well

def area(width, lenght):
    return(width * lenght)
area_ = area(2.4, 5.5)
print("area of room {}".format(area_))
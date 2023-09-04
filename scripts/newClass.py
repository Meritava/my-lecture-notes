
"""
    #write what the module is about - every file in python is a module, a script
"""
class NewClass:
    """
    #at the class level, write documentation for your code
    """
    width = 4
    height = 5

    def __init__(self):
        pass

    def myMethod():
        """
        #always document your code
        """
        return "This is myMethod method"
    
    def __str__(self):
        return("[Rectangle] {}/{}".format(self.width, self.height))





#create an instance of the class
myObj = NewClass()

print(dir(myObj))   #the dir keyword gives you all the attribute and methods that are available in this particular object
"""
controlling the output when you print an object, use the __str__ or __repo__
print(myObj)  #ry this

#we can override either methods or attributes, it means a method or attribute is defined in the general class, but this particular function we are creating we want to override the definition it this function.
"""
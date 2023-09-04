#Live learning session 1st August
"""
first write what the module is about
"""
class NewClass:
    """
    write documentation for the class, this code
    """
    #this is a public attribute, it can be accessed outside the class, it is opened
    width = 4
    height = 5
    #you use a double underscore to declare a private attribute....the private attribute is not accessible outside this class
    __password = "secert"
    #for protected, it can be accessed in the class or any otther class that inhenrits from the class and it is implemented by using a single underscore
    _myname = "Merit Ishekwene"
    #getters and setters are use in regulating private and protected attribute.. so i can put in some logic/requirements for a user to access the password or myname attribute
    #can be either attribute or method
    #getter is to get the value, seter is to set/update the value...so you are creating a public logic/requiremrnt to access the private and protected attribute or method

    """ 
    def __init__(self, email):
        # print(self.__password)   #the attribute is accessed under the class and this method is under the class
        #commented to try something... commented to access password assuming we are not using the init
        self.email = email
    """
    #with email
    def __init__(self, email):
        # print(self.__password)   #the attribute is accessed under the class and this method is under the class
        #commented to try something... commented to access password assuming we are not using the init
        self.email = email
    
    def myMethod(self):
        return "this is my method"
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.width, self.height))
    
    #this is creating the getter to get the password attribute
    @property   #usually to define a method, you bring in the decoration property....when using the at property, you do not need to put parenthesis when calling the method, that is when getting an attribute
    #this method is to access the password private attribute
    def get_password(self):
        return self.__password
    
    """ 
    #creating a setter to change the value
    @get_password.setter
    def get_password(self, newpassword):
        #we want to put a condition that regulates which user can change the atribute value, that was why
        self.__password = "newpassword"
        # return self.__password
    """


     #creating a setter to change the value, putting a condition
    @get_password.setter
    def get_password(self, newpassword):
        #we want to put a condition that regulates which user can change the atribute value
        employee_email = ["merit@gmail.com", "damilare@gmail.com", "merdami@gmail.com"]
        if (self.email in employee_email):
            self.__password = "newpassword"
        # return self.__password

""" 
#create an instance of the class
myObj = NewClass()
print(myObj)
"""

"""

"""


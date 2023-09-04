from newclass import NewClass
""" 
#create an instance of the class and use the height attribute in the class
myObj = NewClass()
print(myObj.height)
# print(myObj.__password)   #this does not print, the secre only printed due to the init method, so anytime and object is creaated from the class, the init method runs
#the myObj object you created from the NewClass, uses the myMethod method/function.. and this is a public method everyone have access to
# print(myObj.myMethod())
print(myObj.get_password)   #gets the password attribute
myObj.get_password = "new password"   #set the password attribute
print(myObj.get_password)
"""
#create an instance of the class and use the height attribute in the class
#with the email
myObj = NewClass("damilare@gmail.com")   #so when creating the object you will have to assign the email, because the email is in the initializing method... you can try changing the value and fill in an email that isnt on the list - this would not allow you to change the password
print(myObj.height)
# print(myObj.__password)   #this does not print, the secre only printed due to the init method, so anytime and object is creaated from the class, the init method runs
#the myObj object you created from the NewClass, uses the myMethod method/function.. and this is a public method everyone have access to
# print(myObj.myMethod())
print(myObj.get_password)   #gets the password attribute
myObj.get_password = "new password"   #set the password attribute
print(myObj.get_password)
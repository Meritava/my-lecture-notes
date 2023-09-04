"""
this is one way of importing a module, you can uncomment to see how it works

# to create a calculator
import add    #how to import a module
#sum
print(add.sum(3, 5))      #using the function in the module
print(add.sumif(4, 4))      #using the function in the module
#sub

#mul

#div
"""

#OR 

from add import sum
from add import sumif
from add import list_1

print(sum(3, 5))
print(sumif(4, 4))
print(list_1)
print(list_1[1]) #it prints the second element on the list




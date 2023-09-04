#! /usr/bin/python3
# list can have same values
"""
LIST IN PYTHON
A list is a collection of items
indexing is the position of each and every item you find on the list... list can have different data type
Examples of list.. the items in the list are called list items or elements
favourite_fruits = ["mango", "apple", "orange", "bananna"]
names = ["merit", "dami", "mercy", 367, 87, ["apple", "mango"]]
"""
favourite_fruits = ["mango", "bananna", "apple", "orange", "bananna"]
print(favourite_fruits)
print(favourite_fruits[1])  #prints the second element in the list
print(favourite_fruits[-1])  #prints the last element on the list 
favourite_fruits[2] = "watermelon" #it replaces the second element
del favourite_fruits[0] #delets the first element
# print(favourite_fruits[-1]) gives you the last item on the list

print(len(favourite_fruits)) #get the length of the list
favourite_fruits.append("pear") #for adding additional element to the list
favourite_fruits.insert(1, "sugarcane") # insert/add an element to the list
favourite_fruits.remove("mango") #used to delete element you can also use this - del favourite_fruits[0] you can als use pop to remove/delete, like this,
# favourite_fruits.pop(), this will delete the last item on the list
print(favourite_fruits)

# example of a while loop this prints the elements in the list
# counter = 0
# while counter < len(favourite_fruits):
#     print(favourite_fruits[counter].upper())
#     counter += 1

# example of a for loop to print the elements in the list
for favorite_fruit in favourite_fruits:
    print(favorite_fruit.lower())

favourite_fruits_copy = favourite_fruits.copy() #this would be a copy of our favorite_fruits
f_c = list(favourite_fruits) #this would be a copy of our favorite_fruits

# concatenating two strings
class_one = ["merit", "mercy", "precious", "gare"]
class_two = ["esther", "tobechi", "sasha"]
total_list = class_one + class_two  # you can also concatenate by doing this -
# class_one.extend(class_two)
# print(class_one) this will add class 2 to class 1
print(total_list)
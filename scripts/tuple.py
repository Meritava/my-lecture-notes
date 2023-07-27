#! /usr/bin/python3
# tuple is a collection and it's content can not be changed
names_executives = ("Merit", "Mercy", "Esther", "Dami", "Esther")
#you can convert a tuple to a list
a = list(names_executives) # the tuple is converted to a list, wih this you can add data to the tuple which is now a list
a.insert = (1, "Cole")
names_executives = tuple(a) # after inserting, you change back to a tuple
print(names_executives) #prints the entire tuple
print(names_executives[0]) #prints the first element in the tuple

#check if an item is on he tuple
if "Merit" in names_executives:
    print("Yes, attended")
else:
    print("No, did not attend")
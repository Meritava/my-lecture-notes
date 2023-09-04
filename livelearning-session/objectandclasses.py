class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, others):
        x_diff_sq = (self.x - others.x) ** 2
        y_diff_sq = (self.y - others.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"    # + plus here represent concatination

c = Coordinate(3, 5)
print(c)   #this is for the __self__ function
zero = Coordinate(0, 0)
print(Coordinate.distance(c, zero))   #this is same as print(c.distance(zero))
print(isinstance(c, Coordinate))
""" 
c = Coordinate(3, 5)
origin = Coordinate(0, 0)
print(c.x)
print(origin.x)
"""


class User:
    def __init__(self, full_name, birthday):
        self.name = full_name   #full_name is the value provided when you create an object while the name attached to the self is the field that stores the value
        self.birthday = birthday



"""
#from python classes, question 1

"""
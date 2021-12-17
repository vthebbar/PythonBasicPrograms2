# Object printing / string representation of object
# str() is used for creating output for end user while repr() is mainly used for debugging and development.
# repr’s goal is to be unambiguous and str’s is to be readable.
class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __repr__(self):  # is a special method used to represent a class's objects as a string.
        return "Value of a=%s and b=%s" %(self.a, self.b)



obj = test(10,20)
print(obj)

class test2:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):   # method in Python represents the class objects as a string
        return "Value of x=%s and y=%s" %(self.x, self.y)


obj2= test2(100,200)
print(obj2)
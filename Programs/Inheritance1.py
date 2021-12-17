# Inheritance

class parent(object):
    def __init__(self):
        print("Base Class constructor")

    def getName(self):
        print("Base class get name")

    def isVeg(self):
        return False

class child(parent):

    def __init__(self, name):
        self.name=name
        print("Name=",self.name)
        print("Child class constructor")

    def isVeg(self):
        return True

# Objects

obj1=parent()
obj1.getName()
print(obj1.isVeg())

obj2 = child("Elephant")
obj2.getName()
print(obj2.isVeg())


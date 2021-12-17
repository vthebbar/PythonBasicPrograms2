# Class , object and constructor

class Animal:
    legs=4

    def __init__(self, name):
        print("Constructor of a class")
        print("name=",name)
        print("Legs=",self.legs)



    def getColor(self, color):
        self.color = color
        print("Color=",self.color)


a=Animal("Elephant")
a.getColor("Black")


# blank class

class test:
    pass

t=test()
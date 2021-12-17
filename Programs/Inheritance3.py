# Multiple Inheritance

class parent1(object):
    def __init__(self):
        print("Parent1")
        self.name="Raj"


class parent2(object):
    def __init__(self):
        print("parent2")
        self.name2="Kumar"

class child(parent1, parent2):

    def __init__(self):
        parent1.__init__(self)
        parent2.__init__(self)

    def getNames(self):
        print(self.name, self.name2)


obj = child()
obj.getNames()


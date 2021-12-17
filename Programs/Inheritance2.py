# Inheritance

class parent(object):
    pass

class child(parent):
    pass

obj1 = parent()
obj2 = parent()

print(issubclass(child, parent))
print(issubclass(parent,child))

print(isinstance(obj1, parent))
print(isinstance(obj2, child))

print(isinstance(obj1,child))
print(isinstance(obj2, parent)) # True


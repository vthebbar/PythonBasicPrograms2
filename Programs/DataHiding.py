# Data hiding

class test:
    __pin=1234  # private/hidden class variable

    def display(self):
        print("Accessing hidden variable inside the class-",self.__pin)


# Crete object
obj=test()
obj.display()

# Accessing private variable
print("Accessing hidden variable outside the class-", obj._test__pin)  # Tricky syntax


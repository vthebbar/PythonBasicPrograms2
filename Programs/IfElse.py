# Use of if else

if True:
    print("True")
else:
    print("False")  # Dead or Unreachable code

if False:
    print("False") # Dead of unreachable code
else:
    print("True")


# Program to find largest of 3 numbers

print("Program to find largest of 3 numbers:")

a=int(input("Key in Value of First Number A="))
b=int(input("Key in Value of Second Number B="))
c=int(input("Key in Value of Third Number C="))

if a>b and a>c:
    print("A is largest")
elif b>c:
    print("B is largest")
elif c>b:
    print("C is largest")
else:
    print("Invalid Input or all are equal")

# Program to find largest of 4 numbers

m=101
n=20
o=5555
p=22

if m>n and m>o and m>p:
    print("M is largest")
elif n>o and n>p:
    print("N is largest")
elif o>p:
    print("O is largest")
elif p>o:
    print("P is largest")
else:
    print("All are euql or Invalid input")


# Use of f string in python to print value
x=100
print("Value of x=", f'{x}')
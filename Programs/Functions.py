# Functions

def sum(a,b):
    print("Sum=",a+b)

sum(10,10)

print("****Function with default or optional argument***")
def getCountry(name="India"):
    print(name)

getCountry()
getCountry("USA")

print("***Function with return value******")

def getCapital(name):
    if name=="India":
        capital="New Delhi"
    elif name == "USA" :
        capital ="Washington"
    elif name == "UK":
        capital="London"
    else:
        capital="Others"
    return capital

res=getCapital("India")
print(res)
res1=getCapital("UK")
print(res1)
print("****************")
def score(list):
    for i in range(0, len(list)):
        print(list[i])

lst=[10,20,80,22,88]
score(lst)

print("**Recursive Function - Factorial****")

def factorial(num):
    if num > 1:
        num = num * factorial(num-1)
    return num

fac=factorial(5)
print(fac)
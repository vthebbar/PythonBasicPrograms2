# use of *args and **kwargs

def sum(*args):
    total=0
    for i in args:
        total=total+i
    print("Total=",total)

sum(1,2,3,4)
sum(10,20,40,50)

print("********************")

def getData(*args):
    for x in args:
        print(x)

getData(1,2,3,4)

print("********* kwargs ************")

def getDetials(**kwargs):
    for key,value in kwargs.items():
        print("%s = %s" %(key,value))

getDetials(id1=10, id2=20)
getDetials(raj=10, ramu=100, bhimu=400, shamu=500)
getDetials(bhoj=4, raa=101)





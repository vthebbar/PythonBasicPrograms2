# Use of for and while Loop

str1 = "I like Python"

for i in str1:
    print(i)

print("******************")

lst1=[1,2,4,9,10]

for i in lst1:
    print(i)

print("******************")

lst2=[100,500,200,600]

for j in range(0,len(lst2)):
    print(lst2[j])

print("*****For with else*************")

for i in range(0,4):
    print(i)
else:
    print("Outside of range")

print("*****While with else*************")
count=0
while count<4:
    print(count)
    count += 1
else:
    print("Else part")

print("*****While *************")

num=0
while num<10:
    print("ok")
    num +=1

print("***********Print pattern***********")

for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()

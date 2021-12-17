# Lists in python

list1=[10,20,30,40,50]
print(list1)

print("5th element is= ",list1[4])

print("Elements from index 0 to 3=",list1[:3])

print("Elements from index 2 to last index",list1[2:])

list1.append(60)
print("Appened list=", list1)

list1.append([1,2,3,4])
print("Appened list to list (Nested list)", list1)

print("Element at index 6 is",list1[6])

print("6th index 1st element of nested list=",list1[6][0])

# remove a elements from list
list1[1:2] =[]  # element at index 1, 2 (20) will be removed

print("After removing element at index 1=",list1)

# remove all elements of a list

list1[:]=[]
print("All elements removed",list1)

list2=[100,200,300,400]
print("List 2 length=", len(list2))

list3=['raj','ram']

print("Conactenate list2 & list3",list2+list3)

print("Last element of list 2 :", list2[-1])

print("Sliced list 2", list2[1:3])  # displays element at index 1 and 2 (element at index 3 is excluded)

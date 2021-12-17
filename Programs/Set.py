# set object / function

# set is a collection of data , it does not allow duplicates, it can store different data types

set1 ={10,20,30,40,50, 50}
print(set1)
print(type(set1))

set1.discard(10)
print(set1)

set2= {"Python"}
print(set2)
print(type(set2))

# set3 = {[10,20,30]} -> can not use list
# print(set3)

# set4 ={ {'name':'raj', 'age':10} } -> Can not use dictionary
# print(set4)

set6 = {(10,20,30)}  # Tuple can be used
print(type(set6))
print(set6)

set7 ={'Raj', 10, 'Ravi', 20}
print(set7)

# mathematical operations
set8={10,20,30,40,50}
set9={40,50,60,70,80}

# Union
print(set8.union(set9))
print(set8|set9)

# intersection
print(set8.intersection(set9))
print(set8 & set9)

# Difference
print(set8.difference(set9))
print(set8-set9)

print(set9.difference(set8))
print(set9-set8)

# Symmetric difference  (remove common elements in both )
print(set8.symmetric_difference(set9))
print(set8^set9)

# Methods

s10= {100,200,300,400,500}
s10.add(600)
print(s10)

s10.remove(100)  # removes existing element, if element is not found gives error
print(s10)

s10.discard(111) # removes if element is present, if element is not present does nothing, no error
print(s10)

s10.discard(400)
print(s10)

s10.update([10,20,30])  # we can add list elements using update
print(s10)


s10.update((1,2,3,4))  # we can add tuple elements using update
print(s10)

s10.update("Python") # we can add string elements using update
print(s10)

s10.update({'raj':111, 'smou':222})  # we can add dictionary  elements using update
print(s10)

s12= s10   # here memory local of s12 and s10 will be same
print(id(s10))
print(id(s12))

s13 =  s10.copy()  # copy method copies to different memory location, memory location of s13 and s10 will be different
print(id(s13))

print(s13)
s13.clear()  # removes all elements of set
print(s13)


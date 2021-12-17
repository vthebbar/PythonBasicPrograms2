# Use of Break and continue

str1="I know python, I do not know odia"

for i in str1:
    if i==',':
        break
    print(i)

print("***Use of continue*******")

for i in str1:
    if i==',':
        continue
    print(i)

print("***Use of Break*******")
plang=['Java','C','C++','Python','dot net','Java Script']

for i in range(0,len(plang)):
    print(plang[i])
    if plang[i]=="Python":
        break

print("***Use of Continue*******")

for i in range(0,len(plang)):
    if plang[i]=="dot net":
        continue   # continue with next iteration, any statements after continue will not be executed for current iteration
    print(plang[i])
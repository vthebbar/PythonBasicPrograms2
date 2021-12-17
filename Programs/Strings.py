# strings

# escape characters \n , \t and \
s1 = "My name is \n vishwa"
print(s1)

s2="My name is \t vishwa"
print(s2)

s3 ='I\'m vishwa'
print(s3)

s4 ="I love \"Python\""
print(s4)

# special string or paragraph inside triple single or triple double quotes

s5=''' This is a para line1
 this is para line 2
 this is para line3'''
print(s5)

s6=""" line 1
line2

line4"""
print(s6)

# in and not in operators

s7="My name is vishwa, I love python"
print("python" in s7) # True

print("Raja" not in s7) # True

# Repeate string using *

print(s7*2)

# sting formatting
print("My name is %s and my age is %d" %("Raj",22))

# is vs ==  -> is compares memory location , == compares values

s8="Welcome to Python"
s9="Welcome to Python"

print(id(s8))
print(id(s9))

print(s8 is s9)
print(s8==s9)

# Built in string methods
s10="  python tutorials program, PYTHON   "

print(s10.capitalize())

print(s10.count("python"))

print(s10.find("python"))

print(len(s10))

print(s10.lower())

print(s10.upper())

print(s10.lstrip())

print(s10.rstrip())

s11="ThisisPython"
print(max(s11))
print(min(s11))


print(s11.split("is"))

print(s11.replace("P","J"))

print(s11[-1]) # refers to last character
print(s11[-2]) # refers to last but one
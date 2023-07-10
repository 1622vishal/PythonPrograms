#----Written by :- Vishal Yadav----#
#----Date :- 10-07-23----# 

"""Program to demonstrate Explicit and Implicit Type Conversion"""

#Explicit TypeCasting

a = "5"
b = "6"

#Output of this will be 56 because anything in double quotes is considered string in python and + sign concatenates these two strings
print(a + b) 

#To get the desired result we have to convert these into int
print(int(a) + int(b))

c = "Hello"
d = "World"
# print(int(c) + int(d))    It cannot convert just any string to int, Remember what you are converting should be valid

#Implicit TypeCasting

x = 34.8
y = 56
z = True    #True will be convrted to 1 and false will be converted to 0 in implicit type casting

print(x + y + z)    #Python will automatically convert int(lower data type) to float(higher order) and answer will be in float

#int to string
print(str(x) + str(y) + str(z))



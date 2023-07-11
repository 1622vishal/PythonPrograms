#----Written by :- Vishal Yadav----#
#----Date :- 11-07-23----# 

"""Program to demonstrate how to embedd variables into strings"""

name = "Vishal Yadav"
age = 20

#String is embedded like this and also we have to use (f) to tell that this string needs to be formatted
#This thing will work like normal print statements
print(f"My name is {name}") 
print(f"{age} is my age")

print("My name is" , name)      #It will generate the same output  (line 11)

#We can also do this 
info = f"{name} is {age} years old"
print(info)

#Since info is also a variable we can embedd this also
print(f"Complete info: {info}")

#If you remove f from this then everything will be printed as it is
info = "{name} is {age} years old"
print(info)
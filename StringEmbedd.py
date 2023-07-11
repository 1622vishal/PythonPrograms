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

"""When triple double quotes are used immediately after a function, class, or module definition, they are treated as docstrings. On the other hand, when triple double quotes are not associated with any specific entity and appear in the middle of the code, they are considered multiline comments.Python recognizes the purpose of triple double quotes based on their location in the code, whether they are associated with a specific entity or appear as standalone blocks."""
multilinestring = """This string is to implement
    multiple line such as poem or essay,
    and it is achieved using triple double or single quotes
    but it is not considered as comments beacause we are assigning
    it to a variable"""

print(multilinestring)
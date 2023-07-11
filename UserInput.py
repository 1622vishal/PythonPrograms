#----Written by :- Vishal Yadav----#
#----Date :- 11-07-23----# 

"""Program to demostrate how to take input from user"""

name = input("Enter your name: ")   #Python gives the flexibility to display msg in input function although it's our choice if we do not want any msg to be displayed

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

#This print function will concatenate the output because input function only takes input in the form of string
print(num1 + num2)

#To get the desired output we have to do typecasting
print(int(num1) + int(num2))

#We can directly store the variable in int form by typecasting them while taking input
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the forth number: "))

#In this way we don't have to convert them each time we use them
print(num3 + num4)

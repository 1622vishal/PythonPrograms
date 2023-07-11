#----Written by :- Vishal Yadav----#
#----Date :- 29-06-23----#

"""Program to demonstrate the use of basic data types"""

a = 5
a1 = 6
b = "Hello"
b1 = "World"
c = True
c1 = False
d = None
e = 4.6   #float
f= complex(5,7)     #complex function will create a complex number and assign it to f
print(a)
print(b)
print(c)
print(d)
print(a + a1)      #Since the data type is int so these two  will be added
print(b + b1)      #The strings will be concatenated
#print(b + 4)       Wrong!!!!!
#print(b - b1)     This i invalid we cannot use - in strings it doesn't make any sense
print(b * 5)       #It will concatenate Hello % times
#print(b * b1)     This is also wrong we cannot multiply two strings 
#print(b / 5)      This is also wrong 
#print(b / b1)
print(c + c1)       #See output
print(f)
# print(a + b)    It will throw error because we cannot add two diff. data types

"""We can also find the data type of variable using type function"""
print("The data type of a is: ", type(a))
print("The data type of b is: ", type(b))
print("The data type of c is: ", type(c))
print("The data type of d is: ", type(d))
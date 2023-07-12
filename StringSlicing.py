#----Written by :- Vishal Yadav----#
#----Date :- 12-07-23----#

"""Program to demostrate how to perform string slicing"""
"""String slicing in Python is a way to extract a portion of a string by specifying a range of indices."""
"""string[start:end:step]"""

state = "Uttar Pradesh"
statelen = len(state)
print(statelen)        #It will print the length of string
print(state[0],state[1],state[4],sep = "")     #This statement will print the character of the string stored at that index
print(state[0],state[1],state[4])

#String Slicing
print(state[0:statelen])
print(state[0:])               #Python takes length of string by default if nothing is specified at end
print(state)
print(state[:])
print("Same Output")
print(state[0:5])          #start = 0 , end = 5
print(state[:8])         #Default start = 0
print(state[2:9])
print(state[9:2])        #When the start index is greater than the end index, the resulting slice will always be an empty string.However you might think that it should print string from backwards but this is not the case
print(state[4:-6])      #It is something like state[4:len(state)-6] and len(state)-6 = 7 => [4:7]
print(state[-8:12])   #Similarly this will work

#String Slicing with step
print(state[0:12:2])    #By default step = 1 and in this case since step is 2 one character will be skipped
print(state[0:13:-2])    #It will print an empty string because start index should be greater than end index
print(state[12:0:-2])

print(state[::-1])    #To print string in reverse direction
print(state[13:0:-1])      #See output
print(state[14:0:-1])      #See output

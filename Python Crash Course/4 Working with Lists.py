# -*- coding: utf-8 -*-

'''
4 working with lists 
page 53(86)
'''

# Looping Through an Entire List 
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
    
    
# A Closer Look at Looping 


# Doing More Work Within a for Loop 
magicians=['alice','david','carolina']

for i in magicians:
    print(i.title()+", that was a great trick!")
    
    
magicians=['alice','david','carolina']

for i in magicians:
    print(i.title()+", that was a great trick!")
    print("I can't wait to see you next trick, "
          +i.title()+"\n")
    
   
# Doing Something after a for Loop 
magicians=['alice','david','carolina']

for i in magicians:
    print(i.title()+", that was a great trick!")
    print("I can't wait to see you next trick, "
          +i.title()+"\n")
    
print("Thank you, everyone. That was a great magic show!")



# Avoiding Indentation Errors 
# Forgetting to Indent 
# Forgetting to Indent Additional Lines 

#Indenting Unnecessarily 
message="Hello Python world!"
    print(message)


# Indenting Unnecessarily After the Loop 


# Forgetting the Colon 
magicians=['alice','david','carolina']
for i in magicians
    print(i)
    

# Making Numerical Lists 
# using the range() function 
for value in range(1,5):
    print(value)


# Using range() to make a list of NUmbers 
numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)


squares=[]
for value in range(1,11):
    square=value**2 
    squares.append(square)
    
print(squares)

#------------------------------------
squares=[]

for i in range(1,11):
    squares.append(i**2)
    
print(squares)


# Simple Statistics with a List of Numbers 
digits=[1,2,3,4,5,6,7,8,9,0]
min(digits)

max(digits)

sum(digits)


# List Comprehension 
squares=[values**2 for values in range(1,11)]
print(squares)


# Working with Part of a List 
players=['charles','martina','michael','florence','eli']
print(players[0:3])

print(players[:4])

print(players[2:])

print(players[-3:])


# Looping Through a Slice 
players=['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
    
# Copying a List 
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

print("My facorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)

#------------------------------------------
# to prove that we actually have two separate lists:
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My facorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)


# This does not work 
'''
This syntax actually tells Python to connect the 
new variable friend_foods to the list that is already 
contained in my_foods, so now both variables point to the same list 
'''
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My facorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)



# Tuple 
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#----------------
dimensions=(200,50)
dimensions[0]=250


# Looping Through all Values in a Tuple 
dimensions=(200,50)
for i in dimensions:
    print(i)


# Writing over a Tuple 
dimensions=(200,50)
print("Original dimensions:")
for i in dimensions:
    print(i)
    
    
dimensions=(400,100)
print("\nModified dimensions:")
for i in dimensions:
    print(i)
    
    





















































































 
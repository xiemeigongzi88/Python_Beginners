# -*- coding: utf-8 -*-
# 3 Introducing Lists 
# page 37(70)

# what is a list?

bicycles=['trek','cannondale','redline','specialized']
print(bicycles)


# Accessing Elements in a list 
print(bicycles[0])

print(bicycles[0].title())


# Index Positions Start at 0 Not 1 
bicycles=['trek','cannondale','redline','specialized']

print(bicycles[1])
print(bicycles[3])


# -1 : python returns the last item in the list 
print(bicycles[-1])


# Using Individual Values from a List 
bicycles=['trek','cannondale','redline','specialized']
message="My first bicycle was a "+bicycles[0].title()+"."
print(message)


# Changing, Adding, and Removing Elements 
# Modifying Elements in a List 
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

# Adding Elements to a List 
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

# the append() method adds 'ducati' to the end of the list 
# without affecting any of the other elements in the list 
motorcycles.append("ducati")
print(motorcycles)


# the append() method makes it easy to build lists dynamically 
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#Inserting Elemtns into a List 

# The insert() method opens a space at position 0 and stores the 
# value 'ducati' at that location 
# This operation shifts every other value in the list one position to the right
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)


# Removing Elements from a List 
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)


motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[2]
print(motorcycles)


# Removing an Item Using the pop() Method 
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

# the value was removed from the end of the list and is now 
# stored in the variable pop_...
pop_motorcycle=motorcycles.pop()
print(motorcycles)
print(pop_motorcycle)


# the pop() method is useful?
motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title())


# Popping Items from any Position in a List 

motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print("The first motorcycle I owned was a "+first_owned.title()+".")


# Removing an Item by Value 

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#-----------------------------------------------
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")


# Organizing a List 
# Sorting a List Pernamently with the sort() Method 
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)


cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)


# Sorting a List Temporarily with the sorted() Function 
cars=['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the orginal list again:")
print(cars)


# Print a List in Reverse Order 
# The reverse() method changes the order of a list permanently,
# but you can revert to the original order anytime by applying reverse() to 
# the same list a second time 
cars=['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)


# Avoiding Index Errors When Working with Lists 
motorcycles=['honda','yamaha','suzuki']
print(motorcycles[3])

print(motorcycles[-1])

motorcycles=[]
print(motorcycles[-1])

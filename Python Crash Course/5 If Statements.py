# -*- coding: utf-8 -*-

'''
5. If Statements 
page 75(108)
'''

# A Simple Example 
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())


# Conditional Tests 

# checking for Equality 
car='bmw'
car=='bmw'

# Ignoring Case When Checking for Equality 
car='Audi'
car.lower()=='audi'

# checking multiple conditions 
age_0=22
age_1=18 
age_0>=21 and age_1>=21



# Checking Whether a Value Is in a List 
requested_toppings=['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings

'pepperoni' in requested_toppings


# checking Whether a Value Is Not in A List 
banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")
    

# Boolean Expressions 
game_active=True
can_edit=False



# if Statements 
# if-else Statements 
# The if-elif-else Chain 

age=12 

if age<4:
    print("Your admission cost is $0")
elif age<18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")


#---------------------------------
age=12

if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
    
print("Your admission cost is $"+str(price))


# Testing Multiple Conditions 
requested_toppings=['mushrooms','onions','pineapple']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding P")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")


#--------------------------------------
requested_toppings=['mushrooms','onions','pineapple']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding P")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")



# Using if Statements with Lists 
# checking for Special Items 
requested_toppings=['mushrooms','green peppers','extra cheese']

for i in requested_toppings:
    print("Adding "+i)
    
print("\nFinished making your pizza!")

#------------------------------------------
requested_toppings=['mushrooms','green peppers','extra cheese']

for i in requested_toppings:
    if i =='green peppers':
        print("Sorry, we are out of green peppers now.")
    else: 
        print("Adding "+i)
    
print("\nFinished making your pizza!")


# Checking That a List is Not Empty 
requested_toppings=[]

if requested_toppings:
    for i in requested_toppings:
        print("Adding "+i)
else:
    print("Are you sure you want a plain pizza?")
    


# Using Multiple Lists 
available_toppings=['mushrooms','olives','green peppers',
                    'pepperoni','pineapple','extra cheese']

requested_toppings=['mushrooms','french fries','extra cheese']

for i in requested_toppings:
    if i in available_toppings:
        print("Adding "+i)
    else:
        print("Soory")
        
print("\nFinish")


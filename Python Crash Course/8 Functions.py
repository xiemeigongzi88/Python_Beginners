# -*- coding: utf-8 -*-

'''
8 Functions 
page 133(166)

'''

# Defining a Function 

def greet_user():
    print("Hello!")
    
greet_user()


# Passing Information to a Function 

def greet_user(username):
    print("Hello, "+username.title()+"!")
    
greet_user('jesse')


# Passing Arguments 
# Positional Arguments 

def describe_pet(animal_type, pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+ "'s name is "+pet_name.title()+".")
    
describe_pet('hamster',"harry")


# Multiple Function Calls 
def describe_pet(animal_type, pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+ "'s name is "+pet_name.title()+".")
    
describe_pet('hamster',"harry")

describe_pet('dog','willie')


# Order Matters in Positional Arguments 
def describe_pet(animal_type, pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+ "'s name is "+pet_name.title()+".")
    
describe_pet("harry",'hamster')


# Keyword Arguments 
def describe_pet(animal_type, pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+ "'s name is "+pet_name.title()+".")
    
describe_pet(animal_type="harry",pet_name='hamster')

describe_pet(pet_name='hamster',animal_type="harry")


# Default Values 
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+ "'s name is "+pet_name.title()+".")
    
describe_pet(pet_name='willie')


# Equivalent Function Calls 
def describe_pet(pet_name,animal_type='dog'):
    






























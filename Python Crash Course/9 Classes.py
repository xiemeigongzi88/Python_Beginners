# -*- coding: utf-8 -*-

# 9 classes 

# creating and using a class 

class Dog():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def sit(self):
        print(self.name.title()+" is now sitting")
        
    def roll_over(self):
        print(self.name.title()+" rolled over!")
        
my_dog=Dog('willie', 6)      

print("My dog's name is "+my_dog.name.title())

print("My dog is "+str(my_dog.age)+" years old")


# accessing attributes 
my_dog.name


my_dog.sit()
my_dog.roll_over()
































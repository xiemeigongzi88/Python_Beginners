# -*- coding: utf-8 -*-

'''
7 User Input and While Loops 
page 117(150)
'''
# How the input() Function Works 

message = input("Tell me sth., and I will repeat it back to you: ")
print(message)

# Writing Clear Prompts 
name=input("Enter your name: ")
print("Hello,"+ name+"!")

#-----------------------------------------
prompt="If you tell us who you are, we can personalize the message you see."

prompt+="\nWhat is your first name?"

name=input(prompt)
print("Hello, "+name)


# Using int() to Accept Numerical Input 
age=input("How old are you?")

age=int(age)
age>=18


# Introducing while Loops 

current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1
    



















































































#!/usr/bin/env python
# coding: utf-8

# # Exc 0: The Setup

# # EXC 1: A Good First Program 

# In[1]:


print("Hello World!")
print("Hello Again!")
print("I like typing this")
print("This is fun")
print("Yay! Printing")
print("I'd much rather you 'not'.")
print('I"said" do not touch this.')


# In[ ]:





# #  EXC2:  Comments and Pound Charaters

# In[2]:


# A comment, this is so you can read your program later
# Anything after the # is ignored by python 

print("I could have code like this.")

# you can also use a comment to 'disable' or comment put a piece of code:
# print "This won't run."

print("This will run.")


# In[ ]:





# In[ ]:





# # EXC 3: Numbers and Math 

# In[3]:


print("I will now count my chickens:")

print("Hens", 25+30/6)

print("Rootsters", 100-25*3%4)


# In[4]:


print("Now I will count the eggs:")

print(3+2+1-5+4%2 -1/4+6)


# In[5]:


print("Is it true that 3+2 < 5-7?")

print(2+3 < 5-7)


# In[6]:


print("What is 3+2?", 3+2)


# In[7]:


print("What is 5-7", 5-7)


# In[8]:


print("Oh, that's why it's False")


# In[9]:


print("How about some more.")


# In[10]:


print("Is it greater?", 5-2)
print("Is it greater or equal?", 5>=-2)
print("Is it less or equal?", 5<=-2)


# In[ ]:





# In[ ]:





# # EXC 4: Variable and Names 

# In[11]:


cars = 100 
space_in_a_car = 4.0 
drivers = 30 
passengers = 90 
cars_not_driven = cars - drivers
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven


# In[12]:


print("There are", cars, "cars available")
print("There are only", drivers, "drivers availabel")
print("There will be", cars_not_driven, "empty cars today")

print("We can transport", carpool_capacity, "people today.")

print("We have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car")


# In[ ]:





# # EXC 5: More Variable and Printing 

# In[22]:


my_name = "Zed A.shaw"
my_age = 35 
my_height = 74
my_weight = 180

my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


# In[14]:


print(f"Let's talk about {my_name}")


# In[16]:


print(f"He's {my_height} inches tall.")


# In[17]:


print(f"He's {my_weight} pounds heavy.")


# In[18]:


print("Actually that's not too heavy.")


# In[19]:


print(f"He's got {my_eyes} eyes and {my_hair} hair.")


# In[20]:


print(f"His teeth are usually {my_teeth} depending on the coffee.")


# In[24]:


total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")


# In[ ]:





# # EXC 6: Strings and Text 

# In[26]:


types_of_people = 10 

x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."


# In[27]:


print(x)


# In[28]:


print(y)


# In[29]:


print(f"I said : {x}")


# In[30]:


print(f"I also said: {y}")


# In[31]:


hilarious = False 
joke_evaluation = "Isn't that joke so funny! {}"


# In[32]:


print(joke_evaluation.format(hilarious))


# In[33]:


w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)


# In[ ]:





# # EXC 7: More Printing 

# In[34]:


print("Mary had a little lamb.")
print("Its fleece was white as {}".format('snow'))


# In[35]:


print("And everywhere that Mary went.")


# In[36]:


print("."*10)


# In[37]:


end1 = "C"
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'


# In[38]:


print(end1+end2+end3+end4 + end5+end6,end="" )


# In[39]:


print(end7+end8+end9+end10+end11+end12)


# In[ ]:





# # EXC 8: Printing, Printing 

# In[40]:


formatter = "{} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your",
                       "Own text here",
                       "Maybe a poem",
                       "Or a song about fear"
                       ))


# In[ ]:





# # EXC 9: Printing， Printing, Printing 

# In[41]:


days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)
print("Here are the months: ", months)


# In[42]:


print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")


# In[ ]:





# # EXC 10: What Was That?

# In[43]:


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# In[ ]:





# # EXC 11: Asking Questions 

# In[44]:


print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# In[ ]:





# # EXC 12: Prompting People 

# In[45]:


age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# In[ ]:





# In[ ]:





# # EXC 13: Parameters, Unpacking, Variables 

# In[46]:



from sys import argv

# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# In[ ]:





# In[ ]:





# # EXC 14: Prompting and Passing 

# In[47]:


from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")


# In[ ]:





# In[ ]:





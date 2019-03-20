
# 2 Variables and simple data types
print("Hello Python World!")


# Variables 
message="Hello Python World!"
print(message)

#Avoiding Name Errors When Using Variables 
message="Hello Python Crash Course reader!"
print(mesage)

mesage="Hello Python Crash Course reader!"
print(mesage)
# in this case, the proram runs successfully


# Strings 
"This is a string"
"This is also a string."

# Changing Case in a String with Methods 
name="ada lovelace"
print(name.title())

name=name.title()
print(name.upper())
print(name.lower())



# Combining or Concatenating Strings 
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name

print(full_name)

print("Hello, "+full_name.title()+"!")

# use concatenation 
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name

message="Hello, "+full_name.title()+"!"
print(message)


# Adding Whitespace to Strings with Tabs or Newlines 
print("\tpython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")


# Stripping Whitespace 
favorite_language="python   "
favorite_language.rstrip()
print(favorite_language)


# remove the whitespace from the string permanently 
favorite_language="python  "
favorite_language=favorite_language.rstrip()
favorite_language


# left side & both sides 
favorite_language="  python  "
favorite_language.rstrip()
favorite_language.lstrip()

favorite_language.strip()


# Avoiding Syntax Errors with Strings 
message='one of Python's strength is its diverse community'

# NUmbers 

# Floats 
0.2+0.1
3*0.1


# Avoiding Type Errors with str() Function 
age=23
message="Happy "+age+" rd Birthday!"
print(message)

age=23
message="Happy "+str(age)+" rd Birthday!"
print(message)


# Comments 


#The zen of Python 
import this

print(this)
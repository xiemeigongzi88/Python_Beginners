# -*- coding: utf-8 -*-

'''
6 Dictionaries 
page 95(128)
'''

# A simple Dictionary 
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])


# Accessing Values in a Dictionary 
alien_0={'color':'green','points':5}

new_points=alien_0['points']
print("You just earned "+str(new_points)+" points")


# Adding New Key_Value Pairs 
alien_0={'color':'green','points':5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)


# Starting with an Empty Dictionary 
alien_0={}
alien_0['color']='green'
alien_0['points']=5

print(alien_0)


# Modifying Values in a Dictionary 
alien_0={'color':'green'}
print("The alien is "+alien_0['color']+".")

alien_0['color']='yellow'
print("The alien is now "+alien_0['color'])

#-----------------------------------

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))

if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
    
alien_0['x_position']=alien_0['x_position']+x_increment

print("New x-position:"+str(alien_0['x_position']))


# Removing Key-Value Pairs 
alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)


# A Dictionary of Similar Objects 
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}

print("Sarah's favorite language is "+
      favorite_languages['sarah'].title()+
      ".")


# Looping Through a Dictionary 
user_0={
        'username':'efermi',
        'first':'enrico',
        'last':'fermi'}

for key, value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)
       
    
#-------------------------------
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}

for name, language in favorite_languages.items():
    print(name.title()+" 's favorite language is "+
          language.title())
    

# Looping Through All the Keys in a Dictionary 
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}

for name in favorite_languages.keys():
    print(name.title())
    
#---------------------------------------
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}
    
friends=['phil','sarah']

for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi "+name.title()+
              ", I see your favorite language is "+
              favorite_languages[name].title()+"!")
  

#-----------------------------------
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

       
      
# Looping Through a Dictionary's Keys in Order 
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}

for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")
    
    
# Looping Through All Values in a Dictionary 
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}

print("The following languages have been mentioned:")
for i in favorite_languages.values():
    print(i.title())
        

#-----------------------------------------
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'}

print("The following languages have been mentioned:")

for i in set(favorite_languages.values()):
    print(i.title())

# wrap set() around a list that contains duplicate items, 
# Python identifies the unique items in the list and builds a set from those items 
    

# Nesting 
# A list of Dictionaries 

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
    
aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)
    
   
#-----------------------------------------
aliens=[]

for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    print(alien)
print(".....")

print("Total number of aliens: "+str(len(aliens)))

#--------------------------------------------
aliens=[]

for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

for alien in aliens[:5]:
    print(alien)
print(".....")

print("Total number of aliens: "+str(len(aliens)))


# A List in a Dictionary 

pizza={
       'crust':'thick',
       'toppings':['mushrooms','extra cheese'],
       }

print("Order a "+pizza['crust']+"-crust pizza "+
      " with the following toppings: ")

for top in pizza['toppings']:
    print("\t" +top)


# A Dictionary in a Dictionary 
    
users={
       'aeinstein':{
               'first':"albert",
               'last':'einstein',
               'location':'princeton'},
       'mcurie':{
               'first':"marie",
               'last':'curie',
               'location':'paris'}}
       
for username, user_info in users.items():
    print("\nUsername: "+username)
    
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']
    
    print(full_name)
    print(location)


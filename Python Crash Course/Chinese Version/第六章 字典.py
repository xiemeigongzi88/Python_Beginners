第六章 字典
page 51- 61 

page 52 
6.1 一个简单的字典
alien_0={"color":"green","point":5}

print(alien_0['color'])

print(alien_0[0])

OUT：
green
  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 5, in <module>
    print(alien_0[0])
KeyError: 0
green

Note:
我记得 字典 是没有顺序的 字典的调用 需要 key 
不能像列表一样 这样调用 a[0]

**********************************
alien_0={"color":"green","point":5}

print(alien_0['color'])

print(alien_0['point'])

OUT：
green
5



page 52 
6.2 使用字典

字典： 
	为  键值对 每个键 都与 一个 值 相关联
	指定键的时候， 将会返回 关联值
	
6.2.1 访问 字典的值

alien_0={"color":"green","point":5}

print(alien_0['color'])

new_points = alien_0['point']
print("you just earned "+str(new_points)+" points")

OUT：
green
you just earned 5 points


6.2.2 添加键值对

字典时一种动态结构， 可以随时往其中添加键值对 
可以依次 指定字典名 用方括号的键 和 相关联的值

alien_0={"color":"green","point":5}

print(alien_0)

alien_0['x_position']=0
alien_0["y_position"]=25

print(alien_0)

OUT：
{'color': 'green', 'point': 5}
{'color': 'green', 'point': 5, 'x_position': 0, 'y_position': 25}


6.2.3 先创建一个空字典

alien_0={}

alien_0['color']='green'
alien_0['points']=5

print(alien_0)

OUT：
{'color': 'green', 'points': 5}


6.2.4 修改字典中的值
alien_0={}

alien_0['color']='green'
alien_0['points']=5

print(alien_0)

alien_0['color']='red'
print(alien_0)

OUT：
{'color': 'green', 'points': 5}
{'color': 'red', 'points': 5}


####################################

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original postion: "+ str(alien_0['x_position']))

if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment

print("new x_position: " +str(alien_0['x_position']))

OUT：
Original postion: 0
new x_position: 2


6.2.5 删除键值对
alien_0={'x_position':0,'y_position':25,'speed':'medium'}

del alien_0['speed']
print(alien_0)

OUT：
{'x_position': 0, 'y_position': 25}

Note：
删除 的 键值对 永远消失了 



6.2.6 由类似对象组成的字典
favorite_langiages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

print("Sarah's favorite language is "+favorite_langiages['sarah'].title()+".")

OUT：
Sarah's favorite language is C.



page 55 
6.3 遍历字典
6.3.1 遍历所有的 键值对 

user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}

for key, value in user_0.items():
    print('\nkey: '+key)
    print('value: '+value)

OUT：
key: username
value: efermi

key: first
value: enrico

key: last
value: fermi

#####################################

favorite_langiages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

for name, language in favorite_langiages.items():
    print(name.title()+"'s favorite language is: "+language.title())
	
OUT：
Jen's favorite language is: Python
Sarah's favorite language is: C
Edward's favorite language is: Ruby
Phil's favorite language is: Python



6.3.2 遍历字典中的所有 键：
favorite_langiages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

for name in favorite_langiages.keys():
    print(name.title())

OUT：
Jen
Sarah
Edward
Phil

####################################
favorite_langiages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

friends=['phil','sarah']

for name in favorite_langiages.keys():
    print(name.title())

    if name in friends:
        print("Hi "+name.title()+", I see you favorite language is "+
              favorite_langiages[name].title()+"!")

OUT：
Jen
Sarah
Hi Sarah, I see you favorite language is C!
Edward
Phil
Hi Phil, I see you favorite language is Python!

###################################
favorite_langiages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

if 'erin' not in favorite_langiages.keys():
    print("Erin, take our pool!")
    
OUT：
Erin, take our pool!


6.3.3 按顺序遍历字典中的所有值

favorite_langiages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

for i in favorite_langiages.values():
    print(i.title())

	
OUT：
Python
C
Ruby
Python

####################
最终的列表可能包含大量的重复项 可以使用集合 set() 
集合类似与列表 但是每一个元素都是独一无二的：

favorite_langiages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

for i in set(favorite_langiages.values()):
    print(i.title())
    
OUT：
C
Ruby
Python



page 58 
6.4 嵌套：

需要将 一系列字典存储在列表中，或者将 列表作为值存储到 字典中 这称之为 嵌套 

可以在列表中嵌套字典 在字典中嵌套列表 
或者在字典中嵌套字典 

6.4.1 字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]

for a in aliens:
    print(a)

OUT：
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}


###################################
aliens=[]

for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")
print('Total number od aliens: '+str(len(aliens)))

OUT：
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
Total number od aliens: 30
	
	
####################################
aliens=[]  ## 列表  

for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10


print("...")
for alien in aliens[0:5]:
    print(alien)

OUT：
...
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}




6.4.2 在字典中存储列表 

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

print('you ordered a '+pizza['crust']+'-crust pizza'+
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t"+topping)
    
OUT:
you ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese


#################################

favorite_language={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for name, languages in favorite_language.items():
    print("\n"+name.title()+ "'s favorite languages are:")
    for language in languages:  ##important the difference between language and languages 
        print("\t"+language.title())

OUT:

Jen's favorite languages are:
	Python
	Ruby

Sarah's favorite languages are:
	C

Edward's favorite languages are:
	Ruby
	Go

Phil's favorite languages are:
	Python
	Haskell     
		
	

6.4.3 在字典中存储字典 
	
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },

    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username,user_info in users.items():
    print("\nUsername:"+username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())
	
OUT：
Username:aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username:mcurie
	Full name: Marie Curie
	Location: Paris


练习没有做

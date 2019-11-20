第八章  函数
page 68- 79 

page 68 
8.1 定义函数

def greet_user():
    '''简单的问候语'''
    print("Hello!")

greet_user()



8.1.1 向函数传递信息 
def greet_user(username):
    '''简单的问候语'''
    print("Hello!"+username.title()+"!")

greet_user("Eric")


8.1.2 实参和形参



page 69 

8.2 传递实参：

8.2.1 位置实参

调用 函数时， python 必须将函数调用中的每个实参都关联到函数定义中的一个形参 

def destribe_pet(animal_type, pet_name):
    """显示宠物信息 """
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+" 's name is "+pet_name.title()+'.')

destribe_pet('hamster','harry')

OUT：
I have a hamster.
My hamster 's name is Harry.


1. 调用函数多次：

def destribe_pet(animal_type, pet_name):
    """显示宠物信息 """
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+" 's name is "+pet_name.title()+'.')

destribe_pet('hamster','harry')
destribe_pet('dog','willie')


2. 位置实参的顺序很重要


8.2.2 关键字实参：
是 传递 给函数的名称- 值对 

def destribe_pet(animal_type, pet_name):
    """显示宠物信息 """
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+" 's name is "+pet_name.title()+'.')

destribe_pet(animal_type='hamster',pet_name='harry')


8.2.3 默认值
编写函数时， 可给每个形参指定默认值 
def destribe_pet(pet_name,animal_type='dog'):
    """显示宠物信息 """
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+" 's name is "+pet_name.title()+'.')

destribe_pet(pet_name='whillie')

Note：
I have a dog.
My dog 's name is Whillie.


Note:
使用默认值时， 在形参列表中 必须先类出 没有默认值的形参， 再列出有默认值的实参， 



8.2.4 等效的函数调用 

def destribe_pet(pet_name,animal_type='dog'):
    """显示宠物信息 """
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+" 's name is "+pet_name.title()+'.')

destribe_pet(pet_name='whillie')
destribe_pet('abel')

destribe_pet('harry','hamster')
destribe_pet(pet_name='harry',animal_type='hamster')
destribe_pet(animal_type='hamster',pet_name='harry')


OUT：
I have a dog.
My dog 's name is Whillie.

I have a dog.
My dog 's name is Abel.

I have a hamster.
My hamster 's name is Harry.

I have a hamster.
My hamster 's name is Harry.

I have a hamster.
My hamster 's name is Harry.


8.2.5 避免实参错误

def destribe_pet(pet_name,animal_type='dog'):
    """显示宠物信息 """
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+" 's name is "+pet_name.title()+'.')

destribe_pet()


OUT：
Traceback (most recent call last):
  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 6, in <module>
    destribe_pet()
TypeError: destribe_pet() missing 1 required positional argument: 'pet_name'


page 72 
8.3 返回值：
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name+" "+last_name
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)

OUT：
Jimi Hendrix


8.3.2 让实参变成可选的：
def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name+" "+middle_name+" " +last_name
    return full_name.title()

musician=get_formatted_name('jimi','lee','hendrix')
print(musician)

OUT：
Jimi Lee Hendrix

############################################3
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name: ##存在
        full_name = first_name+" "+middle_name+" " +last_name
    else:
        full_name = first_name +" " + last_name

    return full_name.title()

musician=get_formatted_name('jimi','hendrix','lee')
print(musician)


page 73 
8.3.3 返回字典
def build_person(first_name, last_name):
    person={'first':first_name,'last':last_name}
    return person

musician=build_person('jimi','hendrix')
print(musician)

OUT：
{'first': 'jimi', 'last': 'hendrix'}


8.3.4 结合使用 函数 和 while 循环 

def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name=input("First name:")
    l_name=input("Last name:")

    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name())

	
	#######################
退出条件：
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name=input("First name:")
    if f_name =='q':
        break
        
    l_name=input("Last name:")
    if l_name=='q':
        break
    
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name())


page 74 
8.4 传递列表：
 def greet_users(names):

    for name in names:
      msg="Hello "+name.title()+"!"
      print(msg)

usernames=['ada','eric','abel']
greet_users(usernames)

OUT:
Hello Ada!
Hello Eric!
Hello Abel!


8.4.1 再函数中修改列表
将列表传递给函数以后， 函数就可以对其修改，
在函数中对这个列表的任何 修改都是永久性的 


unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

while unprinted_designs:
    current_design=unprinted_designs.pop()

    print("Model: "+current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

OUT：
Model: dodecahedron
Model: robot pendant
Model: iphone case

The following models have been printed: 
dodecahedron
robot pendant
iphone case



##################################################
def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design=unprinted_designs.pop()

        print("Model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe follwoing models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


//OUT：
Model: dodecahedron
Model: robot pendant
Model: iphone case

The follwoing models have been printed: 
dodecahedron
robot pendant
iphone case



8.4.2 禁止函数修改列表：
可以向函数传递副本 而不是原件 
这样函数所作的任何修改都只影响副本 不影响原件

function_name(list_name[:])

切片表示法[:] 创建列表的副本 

print_models(unprinted_designs[:],completed_models)



page  76 
8.5 传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepper')
make_pizza('mushrooms','green peppers','extra cheese')

形参让 python 创建一个名为 toppings 的空元组， 并将收到的所有值都封装在这个元组中， 
Note：
	python 将实参封装到一个元组中， 即便这个函数只收到一个值  
	
##############################################
def make_pizza(*toppings):
    print("\n making a pizza with the follwing toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza('pepper')
make_pizza('mushrooms','green peppers','extra cheese')

OUT：
 making a pizza with the follwing toppings:
- pepper

 making a pizza with the follwing toppings:
- mushrooms
- green peppers
- extra cheese


8.5.1 结合使用位置 实参和 任意数量实参 
如果让函数接受不同类型的实参， 必须在函数定义中将接纳任意实参的形参 放在最后

python 先匹配位置实参 和 关键字实参，
再将余下的实参都收集到最后一个形参中 

def make_pizza(size, *toppings):
    print("\nMaking a "+str(size)+ "inch pizza with the following toppings:")

    for topping in toppings:
        print("- "+topping)

make_pizza(16,'pepper')
make_pizza(12,"mushrooms","green peppers","extra cheese")


OUT：

Making a 16inch pizza with the following toppings:
- pepper

Making a 12inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese


8.5.2 使用任意数量的关键字实参

def build_profile(first,last,**user_info):

    profile=dict()

    profile["first_name"]=first
    profile["last_name"]=last

    for key,value in user_info.items():
        profile[key]=value

    return profile

user_profile=build_profile('albert','einstein',location='princeton',field='physics')

print(user_profile)

OUT：
{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}


8.6 将函数存储再模块中


def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")

    for topping in toppings:
        print("="+topping)

		
import pizza

pizza.make_pizza(16,'pepper')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')


可以使用下面的语法来使用任何一个函数：
module_name.function_name()



8.6.2 导入特定的函数




8.6.3

page 79  
8.7 函数编写指南 








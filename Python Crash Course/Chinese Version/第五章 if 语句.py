第五章 if 语句 
page 43 - 51 

Page 43 
5.1 一个简单示例

cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

        
OUT：
Audi
BMW
Subaru
Toyota



Page 43
5.2 条件测试

5.2.1 检查是否相等
>>> car='bmw'
>>> car=='bmw'
True

>>> car=='audi'
False


5.2.2 检查是否相等时 不考虑大小写 
两个大小写不同的值 会被视为 不相等 
>>> car='Audi'
>>> car=='audi'
False


>>> car='Audi'
>>> id(car)
1726721382080
>>> car_1=car.lower()
>>> print(car_1)
audi
>>> id(car_1)
1726721296400
>>> car_1=='audi'
True
>>> car
'Audi'

Note：
函数 lower() 不会修改存储在 变量 car 中的值， 因此， 使用 lower() 函数 不会改变原来的变量 

5.2.3 检查是否不相等 
requested_topping='mushrooms'

if requested_topping!='anchovies':
    print("Hold the it!")
	
Hold the it!


5.2.4 比较数字：
>>> age=18
>>> age==18
True


answer=17

if answer !=42:
    print("That is not the correct answer. try again!")
	
OUT：
That is not the correct answer. try again!

数学比较：
=
<
>
<=
>=


5.2.5 检查多个条件
1. 使用 and 检查多个条件

age_0=22
age_1=18

print(age_0 >=21 and age_1>=21)

age_1=22

print(age_0 >=21 and age_1>=21)


OUT：
False
True


2. 使用 or 检查多个条件
age_0=22
age_1=18

print(age_0 >=21 or age_1>=21)

age_0=18

print(age_0 >=21 or age_1>=21)


OUT：
False
True


5.2.6 检查特定值是否包含在列表中 in
a=['mushrooms','onions','pineapple']

print('mushrooms' in a)

print('pepper' in a)

OUT:
True
False

Note :
	关键字 in 能够 在创建一个列表后， 检查其中是否包含特定的值
	

5.2.7 检查特定值 是否不包含在列表中 
关键字 not in 

users=['abel','eric','divid']
user='ana'

if user not in users:
    print(user.title()+", you can post a response if you wish.")
    
OUT:
Ana, you can post a response if you wish.


5.2.8 布尔表达式
True 
False 

car='honda'

print(car=='honda')

print(car=='audi')

OUT:
True
False


5.3 if 语句
最简单的 if 语句 只有一个 测试 和 一个操作：


age =19

if age>=18:
    print('you are old enough to vote!')
    print('Have you registered to vote yet?')
    
OUT：
you are old enough to vote!
Have you registered to vote yet?


5.3.2 if-else 语句
age =17

if age>=18:
    print('you are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote!')
    print('register to vote as soon as you turn 18!')

OUT：

Sorry, you are too young to vote!
register to vote as soon as you turn 18!


5.3.3 if-elif-else 结构 
age=12 

if age<4:
    print("admission cost: 0 ")
elif age<18:
    print("admission cost: 5")
else:
    print('admission cost: 10')
	
OUT：
admission cost: 5

####################################

age=12 

if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
    
print("admission cost:"+str(price))

OUT：
admission cost:5


5.3.4 使用多个 elif 代码块

age=12

if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=5

print("admission fee:"+str(price))

print("admission cost:"+str(price))

OUT：
admission fee:5
admission cost:5


5.3.5 省略 else 代码块
age=12

if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10


print("admission fee:"+str(price))



5.3.6 测试多个条件


requested_topping=['mushrooms','cheese']

if 'mushrooms' in requested_topping:
    print("adding mushroom.")

if 'pepper' in requested_topping:
    print('adding pepper.')

if 'cheese' in requested_topping:
    print('adding cheese.')

print('\n')

OUT：
adding mushroom.
adding cheese.

#####################
如果使用 if-elif-else 结构 代码不能正确运行 

requested_topping=['mushrooms','cheese']

if 'mushrooms' in requested_topping:
    print("adding mushroom.")

elif 'pepper' in requested_topping:
    print('adding pepper.')

else 'cheese' in requested_topping:
    print('adding cheese.')

print('\n')

OUT：
    else 'cheese' in requested_topping:
                ^
SyntaxError: invalid syntax  语法；句法；有秩序的排列



Page 49 
5.4 使用 if 语句处理列表
5.4.1 检查特殊元素 

requested_toppings=['mushrooms','pepper','cheese']

for i in requested_toppings:
    print("adding "+i)

print('\nFinish your pizza')

OUT：
adding mushrooms
adding pepper
adding cheese

Finish your pizza


#########################################

requested_toppings=['mushrooms','green pepper','cheese']

for i in requested_toppings:
    if i =='green pepper':
        print("sorry, we are out of green pepper now ")
    else:
        print("adding "+i)

print('\nFinish your pizza')

OUT：
adding mushrooms
sorry, we are out of green pepper now 
adding cheese

Finish your pizza


5.4.2 确定列表不是空的
requested_toppings=['mushrooms','green pepper','cheese']

if requested_toppings: 
## 不是空列表 
    for i in requested_toppings:
        print("adding "+i.title())
        
    print("\n finished making your pizza")
    
else:
    print("are you sure you want a plaint pizza?!")
    
OUT：
adding Mushrooms
adding Green Pepper
adding Cheese

finished making your pizza

######################################
requested_toppings=[]

if requested_toppings:
    for i in requested_toppings:
        print("adding "+i.title())

    print("\nfinished making your pizza")

else:
    print("are you sure you want a plaint pizza?!")

OUT：
are you sure you want a plaint pizza?!



5.4.3 使用多个列表：

available_topings=['mushrooms','olives','green peppers','pepperoni','pineapple','cheese']

requested_toppings=['mushrooms','french fries','cheese']

for i in requested_toppings:
    if i in available_topings:
        print("adding"+i)
    else:
        print("sorry, we don't have"+i)

print('\nfinished')

OUT：
adding mushrooms
sorry, we don't have french fries
adding cheese

finished


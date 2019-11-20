第七章 用户输入 和 while 循环 
page 61- 68 

page 62 

7.1 函数 input() 的工作原理
message=input("tell me something, and I will repeat it back to you: ")
print(message)

OUT:
tell me something, and I will repeat it back to you:
far far far away
far far far away



7.1.1 编写清晰的程序

name=input("please enter your name: ")
print("Hello, "+name+"!")

OUT:
please enter your name: Eric
Hello, Eric!

有的时候， 提示可能超过一行 
可将提示存储在一个变量中， 再将该变量传递给函数 input() 

prompt="If you tell us who you are,we can personalize the message you see."
prompt+="\n What is your first name?"

name =input(prompt)
print("\nHello, "+name+"!")

OUT:

If you tell us who you are,we can personalize the message you see.
 What is your first name?Eric

Hello, Eric!



7.1.2 使用 int() 来获取数值输入 
使用函数 input() ， python将 用户输入解读为字符串

age=input("how old are you?")
print(age)

OUT：
how old are you?21
21

Note：
21 是字符串 

######################
>>> age=input("How old are you?")
How old are you?21
>>> age
'21'
>>> age>=18
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    age>=18
TypeError: '>=' not supported between instances of 'str' and 'int'

##################################
函数 int() 将数字的字符串表示为数值表示

>>> age=input("How old are you?")
How old are you?18
>>> age
'18'
>>> age=int(age)
>>> age>=15
True


#######################################
height=input("how tall are you, in inches?")
height=int(height)

if height>=36:
    print("\nYou are tall enghou to ride!")
else:
    print("\nYou'll be able to ride when you are a little older.")
	
OUT:
how tall are you, in inches?71

You are tall enghou to ride!


7.1.3 求模运算符

>>> 4%3
1
>>> 5%3
2
>>> 6%2
0
>>> 7%3
1


number =input("enter a number，and I ll tell you if its even or odd")
number=int(number)

if number %2 ==0:
    print(str(number)+" is even.")
else:
    print(str(number) + ' is odd.')
	
OUT：
enter a number，and I ll tell you if its even or odd21
21 is odd.



page 64 
7.2 while 循环简介 
current_number=1

while current_number <=5:
    print(current_number)
    current_number+=1
	
OUT：
1
2
3
4
5



7.2.2 让用户选择何时退出

prompt="\nTell me something, and i will repeat it back to you."
prompt+="\nEnter quit to end the program."

message=""
while message!='quit':
    message=input(prompt)
    
	if message!='quit'
		print(message)

    
7.2.3 使用标志 
prompt="\nTell me something, and i will repeat it back to you."
prompt+="\nEnter quit to end the program."

active =True
while active:
    message=input(prompt)

    if message=='quit':
        active=False
    else:
        print(message)
		
		
7.2.4 使用 break 退出循环

prompt="\nTell me something, and i will repeat it back to you."
prompt+="\nEnter quit to end the program."

while True:
    city=input(prompt)

    if city=='quit':
        break
    else:
        print("I d love to go to "+city.title()+"!")
	
OUT：


7.2.5 再循环中使用 continue 

current_number=0
while current_number<10:
    current_number+=1

    if current_number%2 ==0:
        continue

    print(current_number)
	
OUT:
1
3
5
7
9


7.2.6 避免无限循环
x=1
while x<=5:
    print(x)
	
终止循环：

ctrl+c 
	
	
	
Page 66 
7.3 使用 while 循环来处理列表和字典 
7.3.1 在列表之间移动元素 

unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

while unconfirmed_users:
## 列表作为循环条件 
    current_user=unconfirmed_users.pop()

    print("verifying user:"+current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for user in confirmed_users:
    print(user)
    
OUT：
verifying user:Candace
verifying user:Brian
verifying user:Alice

The following users have been confirmed: 
candace
brian
alice


7.3.3 使用用户输入来填充字典：
responses={}  #dict() 也可以

polling_active=True

while polling_active:
    name=input("\nWhat is your name?")
    response=input("which mountain would you like to climb today?")

    responses[name]=response

    repeat=input("would you like to let another person respond?(yes or no)")

    if repeat=='no':
        polling_active=False


print("\n --- Polling Results ---")

for name, response in responses.items():
    print(name+" would like to climb "+response+".")






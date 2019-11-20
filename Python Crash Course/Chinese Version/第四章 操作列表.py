第四章 操作列表
page 33- 42
4.1-4.7

page 33 
4.1 遍历整个列表 

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
	
OUT：
alice
david
carolina


4.1.1 深入地研究循环 

Note：
	对列表中的每个元素， 都将执行循环指定的步骤， 而不管列表包含有多少元素 
	
	编写 for 循环， 对于 用于 存储列表中每个值得临时变量 可以指定任何名称
	

4.1.2 在 for 循环中执行 更多的 操作 

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a greatr trick!")
	
OUT：
Alice, that was a greatr trick!
David, that was a greatr trick!
Carolina, that was a greatr trick!


######################################

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a greatr trick!")
    print("I cant wait to see your next trick, "+magician.title()+".\n")
	
OUT：
Alice, that was a greatr trick!
I cant wait to see your next trick, Alice.

David, that was a greatr trick!
I cant wait to see your next trick, David.

Carolina, that was a greatr trick!
I cant wait to see your next trick, Carolina.


4.1.3 在 for 循环结束后执行一些操作 

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a greatr trick!")
    print("I cant wait to see your next trick, "+magician.title()+".\n")

print("Thank you,everyone. That was a great magic show!")


OUT：
Alice, that was a greatr trick!
I cant wait to see your next trick, Alice.

David, that was a greatr trick!
I cant wait to see your next trick, David.

Carolina, that was a greatr trick!
I cant wait to see your next trick, Carolina.

Thank you,everyone. That was a great magic show!



Page 35 
4.2  避免缩进错误 

4.2.1 忘记缩进

magicians=['alice','david','carolina']
for magician in magicians:
print(magician.title()+", that was a greatr trick!")

OUT：
  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 3
    print(magician.title()+", that was a greatr trick!")
        ^
IndentationError: expected an indented block


4.2.2 忘记缩进额外的代码行

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a greatr trick!")

print("\nI cant wait to see your next trick, "+magician.title()+".\n")

OUT：
Alice, that was a greatr trick!
David, that was a greatr trick!
Carolina, that was a greatr trick!

I cant wait to see your next trick, Carolina.


4.2.3 不必要的缩进 
message="Hello Python World!"
    print(message)
	
OUT：
    print(message)
    ^
IndentationError: unexpected indent


4.2.4 循环后不必要的缩进

4.2.5 遗漏了冒号：



Page 36 - 42 
4.3 创建数值列表：

4.3.1 使用函数 range() 
for value in range(1,5):
    print(value)

OUT:
1
2
3
4


4.3.2 使用 range() 创建数字列表
numbers=list(range(1,6))
print(numbers)

OUT:
[1, 2, 3, 4, 5]

##############################

even_numbers=list(range(2,11,2))
print(even_numbers)

OUT:
[2, 4, 6, 8, 10]


odd_numbers=list(range(1,12,2))
print(odd_numbers)

OUT:
[1, 3, 5, 7, 9, 11]

##############################

squares=[]
for i in range(1,11):
    square=i**2
    squares.append(square)

print(squares)

OUT:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

or:

squares=[]
for i in range(1,11):
    squares.append(i**2)

print(squares)

OUT:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


4.3.3 对数字列表执行简单的统计计算 
digits=list(range(0,10))
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

OUT：
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0
9
45


4.3.4 列表解析 
squares=[i**2 for i in range(1,11)]
print(squares)

OUT：
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#################################
EXC 4-3
 
for i in range(1,21):
    print("\t"+str(i))
	

EXC 4-4 
a=list(range(1,1000001))

for i in a:
    print(i)
	
	
EXC 4-5 
a=list(range(1,1000001))

for i in a:
    print(i)

print(min(a))
print(max(a))

print(sum(a))


EXC 4-6 
a=list(range(1,20,2))

for i in a:
    print(i)
	

EXC 4-7 
a=list(range(3,31,3))

for i in a:
    print(i)
	
	
EXC 4-8 
a=[x**3 for x in range(1,11)]
print(a)

for i in a:
    print(i)
	
	
EXC 4-9 


Page 38 -42 
4.4 使用列表的一部分 
            0       1       2     3      4      5 
players=['abel','martina','eli','ada','eric','micheal']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

OUT：
['abel', 'martina', 'eli']
['martina', 'eli', 'ada']
['abel', 'martina', 'eli', 'ada']
['eli', 'ada', 'eric', 'micheal']
['ada', 'eric', 'micheal']


4.4.2 遍历切片
players=['abel','martina','eli','ada','eric','micheal']

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())
	
OUT：

Here are the first three players on my team:
Abel
Martina
Eli


4.4.3 复制列表 

my_foods=['pizza','falafel','carrot','cake']

friends_foods=my_foods[:]

print("my favorite foods are:")
print(my_foods)

print("\nmy frind s favorite foods are:")
print(friends_foods)


OUT：
my favorite foods are:
['pizza', 'falafel', 'carrot', 'cake']

my frind s favorite foods are:
['pizza', 'falafel', 'carrot', 'cake']

	
#########################################

my_foods=['pizza','falafel','carrot','cake']

friends_foods=my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)

print("\nmy frind s favorite foods are:")
print(friends_foods)


OUT：
my favorite foods are:
['pizza', 'falafel', 'carrot', 'cake', 'cannoli']

my frind s favorite foods are:
['pizza', 'falafel', 'carrot', 'cake', 'ice cream']

###################################

	
my_foods=['pizza','falafel','carrot','cake']

friends_foods=my_foods # important 
# 这里将 my_foods 赋给 friends_foods 而不是 将
# my_foods 的副本存储到 friends_foods 
# 这种语法 让 两个变量都指向同一个列表 
# 所以 后面出现 'cannoli'  && 'ice cream'

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)

print("\nmy frind s favorite foods are:")
print(friends_foods)


OUT：
my favorite foods are:
['pizza', 'falafel', 'carrot', 'cake', 'cannoli', 'ice cream']

my frind s favorite foods are:
['pizza', 'falafel', 'carrot', 'cake', 'cannoli', 'ice cream']

##########################################3

EXC  4-10 
打印 "The first three items in the list are:", 使用切片 打印前三个元素 

a="The first three items in the list are:"
print(a)
b=a.split()
print(b)

for i in b[:3]:
    print(i)

OUT：
The first three items in the list are:
['The', 'first', 'three', 'items', 'in', 'the', 'list', 'are:']
The
first
three


打印消息 “Three items from the middle of the list are:”
再使用切片来打印列表中间的三个元素 

a="Three items from the middle of the list are:"
print(a)
b=a.split()
print(b)

cnt=len(b)
print(cnt)

for i in b[cnt//2-1:cnt//2+2]:
    print(i)
	
OUT：
Three items from the middle of the list are:
['Three', 'items', 'from', 'the', 'middle', 'of', 'the', 'list', 'are:']
9
the
middle
of


打印消息 "The last three items in the list are:"
a="The last three items in the list are:"
print(a)
b=a.split()
print(b)

for i in b[-3:]:
    print(i)
	
OUT:
['The', 'last', 'three', 'items', 'in', 'the', 'list', 'are:']
8
the
list
are:



Page 41 
4.5 元组 
列表是可以修改的 不可改变的列表是 元组 

4.5.1 定义元组：

dimensions=(200,5)
print(dimensions[0])
print(dimensions[1])

dimensions[0]=98

OUT：

200
5
Traceback (most recent call last):
  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 5, in <module>
    dimensions[0]=98
TypeError: 'tuple' object does not support item assignment


4.5.2 遍历元组中的所有值
dimensions=(200,5)

for dimension in dimensions:
    print(dimension)
	
OUT：
200
5


4.5.3 修改 元组变量
dimensions=(200,5)

print("Original dimensions:")

for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions:")

for dimension in dimensions:
    print(dimension)

OUT：
Original dimensions:
200
5

Modified dimensions:
400
100

Note：	
	给元组变量赋值时合法的 

	
	
EXC 4-13 

	

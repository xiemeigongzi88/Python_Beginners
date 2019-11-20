4 控制语句
051- 066 

051. 安装 PyCharm

052. 单分支选项结构  条件表达式 
print("Hello PyCharm!")

'''num = input("enter a number:")
if int(num) < 10:
    print(num)
'''

a = 3
if a<10:
    print(a)



a=input("enter a number:")

if int(a)<10:
    print(a)

	
测试 条件表达式 

if 3:
	print("ok")
	

a=[]
if a:
	print("空列表， False")
	

	
s="False"
if s:
	print("非空字符串， True")
	
	
c=9
if 3<c<20
	print("3<c<20")
	

if 3<c and c<20
	print("3<c and c<20")
	
if True:
	print("true")
	
	
##################################
if 3:
    print("ok")

a = []
if a:  #不会打印
    print("空列表， False")

if not a:  # 不会打印
    print("非空列表， True")

s = "False"
if s:
    print("非空字符串， True")

d=0
if d:
    print("True")
else:
    print("False")  ##


c = 9
if 3 < c < 20:
    print("3<c<20")


if 3 < c and c < 20:
    print("3<c and c<20")

if True:
    print("true")

OUT:

ok
非空列表， True
非空字符串， True
False
3<c<20
3<c and c<20
true

# 条件判断 语句 不能 出现赋值语句  赋值符


053. 双分支选择结构

s=input("enter one number")

if int(s)<10:
	print("s<10")
else:
	print("s>=10")
	
	
三元条件运算符：
条件为真的值 if(条件表达式) else  条件为假的值

num=input("enter one number")
print(num if int(num)<10 else "too large")



054. 多分枝选择结构

#测试多分支选择结构
score = int(input("enter a number"))
grade = ""

if score<60:
    grade = "F"
elif score < 80:
    grade ="C"
elif score < 90:
    grade = "B"
elif score < 100:
    grade = "A"

print("分数是{0},等级是{1}".format(score,grade))


#打印坐标的象限

x=int(input("enter x number:"))
y=int(input("enter y coordinate:"))

if(x==0 and y==0):
	print("(0,0)")
elif (x==0):
	print("Y axis")
elif (y==0):
	print("X axis")
elif (x>0 and y>0):
	print("First")
elif (x>0 and y<0):
	print("Second")
elif (x<0 and y<0):
	print("Third")
elif (x<0 and y>0):
	print("Forth")

	
	
	

055. 选择结构的嵌套 

控制 缩进量

score = int(input("enter a number:"))

if (score<0 or score >100):
	score=int(input("enter right number:"))
else:
	if(score>=90):
		print("A")
	elif(score>=80):
		print("B")
	elif(score>=70):
		print("C")
	elif(score>=60):
		print("D")
	else:
		print("F")


		
		
056. 循环结构 while 循环 死循环处理

num=0

while (num<=10):
	print(num)
	num+=1
	

计算 1-100 数字的累加和
sum=0
i=0

while sum <=100:
	sum+=i
	i+=1
	
print(sum)
	
	

057. for 循环 遍历各种可迭代的对象

for 变量 in  可迭代对象
	循环体语句 
	
	
for x in (20,30,40)
	print(x+30)
	
	
for x in (20,30,40):
	print(x+30)


for x in list("sxt Python PyCharm")
	

for x in "abcdefg":
    print(x)
	
	
遍历字典：

d={"name":"Abel", "age":18, "job":"programmer"}

for x in d:
	print(x)
	
OUT:
name
age
job



for x in d.keys():
    print(x)

for x in d.values():
    print(x)

for x in d.items():
    print(x)
	
OUT:
name
age
job
name
age
job
Abel
18
programmer
('name', 'Abel')
('age', 18)
('job', 'programmer')



for i in range(1,10,2):
    print(i)
	
	
sum=0
sum_odd=0
sum_even=0

for x in range(101):
	sum+=x
	if(x%2==0):
		sum_even+=x
	else :
		sum_odd+=x
		
print(sum)
print(sum_even)
print(sum_odd)

OUT:

5050
2550
2500



058. 嵌套循环
# done by myself 

num=0

for x in range(5)
	for y in range(5)
		print(num,end=" ")
		
	print()
	num+=1

OUT:
0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 


# done by book 

for x in range(5):
	for y in range(5):
		print(x,end="\t")
	print()
	
	
	
059. 九九乘法表

for m in range(10):
	for n in range(1,m+1):
		print("{0}*{1}=".format(m,n,(m*n)),end="\t")
		
	print()


用列表 和 字典存储信息 并打印 > 15000 的信息

tb=[]
r1=dict(name="Abel",age=18,salary=3000,city="Beijing")
r1=dict(name="Eric",age=20,salary=1000,city="Beijing")
r1=dict(name="Ana",age=18,salary=2000,city="Beijing")

tb=[r1,r2,r3]

for x in tb:
	if x.get("salary")>1500
		print(x)

OUT：
{'name': 'Abel', 'age': 18, 'salary': 3000, 'city': 'Beijing'}
{'name': 'Ana', 'age': 18, 'salary': 2000, 'city': 'Beijing'}




060. break 语句 

>>> a="jfirenfjre"
>>> a.upper()
'JFIRENFJRE'


while True:
	a=input()
	if a.upper()=='Q':
		print("end")
		break
	else:
		print(a)
		
		
061. continue  
empNum=0
salarySum=0
salaries=[]

while True:
	s=input("end with Q or q")
	
	if s.upper=='Q':
		print("finish,and quit")
		break
		
	if float(s)<0:
		continue
		
	empNum+=1
	salaries.append(float(s))
	salarySum+=float(s)
	

print("The number of imployee:{0}".format(str(empNum)))



062. else 语句 

	while for 循环可以附带一个 else 语句（可选）。
	如果循环语句没有被 break 语句结束， 则会 执行 else 语句 
	
while 条件表达式：
	循环体语句
else：
	语句块

empNum=0
salarySum=0
salaries=[]

for i in range(4):
	s=input("end with Q or q")
	
	if s.upper=='Q':
		print("finish,and quit")
		break
		
	if float(s)<0:
		continue
		
	empNum+=1
	salaries.append(float(s))
	salarySum+=float(s)
		
	
else:
	print("录入4 个内容")
	
	

063. 循环代码优化技巧
1. 尽量减少循环内部不必要的计算 
2. 嵌套循环 减少内层循环的计算 尽可能向外提
3. 局部变量查询快 尽量用局部变量


064. zip() 并行迭代
可以通过 zip() 函数 对多个序列并行迭代 
zip() 函数 在最短序列 “ 用完 ” 时会停止

for i in [1,2,3]:
	print(i)
	
	
names=("Eric","Abel","Ana","Wisper")
ages=(18,16,20,35)
jobs=("teacher","student","officer","programmer")

for name,age, job in zip(names,ages,jobs)
	print("{0}--{1}--{2}".format(name,age,job))



065. 推导式 创建序列 

列表推导式：
	生成列表对象 
	
	[表达式 for item in 可迭代对象]
	[表达式 for item in  可迭代对象 if 条件判断]
	
[x*2 for x in range(1,5)]
[2, 4, 6, 8]


>>> [x*2 for x in range(1,5)]
[2, 4, 6, 8]
>>> y=[x*2 for x in range(1,50) if x%5==0]
>>> print(y)
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> 


>>> y=[]
>>> for x in range(1,5):
	y.append(x*2)
>>> print(y)
[2, 4, 6, 8]


cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print(cells)




字典推导式
{key_expression: value_expression for 表达式 in  可迭代对象}

类似与列表推导 字典也可以增加 if   for 
my_text ='I love you, I love sex, I love Ada.'
char_count={c:my_text.count(c) for c in my_text}

>>> char_count
{'I': 3, ' ': 8, 'l': 3, 'o': 4, 'v': 3, 'e': 4, 'y': 1, 'u': 1, ',': 2, 's': 1, 'x': 1, 'A': 1, 'd': 1, 'a': 1, '.': 1}



集合推导
>>> b={x  for  x in range(1,100) if x%9==0}
>>> b
{99, 36, 72, 9, 45, 81, 18, 54, 90, 27, 63}

# 集合不可重复 


生成器推到式 （生成元组）
一个 生成器 只能使用一次 
元组时没有推导式的

>>> gnt=(x for x in range(4))
>>> print(gnt)
<generator object <genexpr> at 0x000001E48D086A98>

>>> print(tuple(gnt))
(0, 1, 2, 3)
>>> print(tuple(gnt))
()
# 生成器只能用一次  时可迭代对象 可被循环 

>>> for x in gnt:
	print(x,end=" ")

	
>>> 
>>> 

# 空了 无法打印 

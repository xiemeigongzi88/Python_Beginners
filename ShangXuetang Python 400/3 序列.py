3.序列

032. 列表 特点 内存分析 
序列是一种数据存储方式， 用来存储一系列的数据
在内存中 序列就是一块用来存放多个值的连续内存空间 

列表是 内置可变序列 是 包含多个元素的有序连续内存空间 
a=[10,20,30,40]

a=[10,20,'abc',True]

list.append(x)： 将元素 x 加到 list 尾部
list.extend(aList): 将列表 alist 所有元素加到 list 尾部
list.insert(index,x) : 在列表中指定位置 插入 元素 x 
list.remove(x): 删除list 中 首次 出现的元素 x 

list.pop([index]): 删除元素 并返回list 指定位置 index 的元素，默认是最后一个元素
list.clear(): 删除所有元素 只是删除列表里所有的元素 并不是删除列表对象
list.index(x): 返回第一个 x 元素的索引位置 如 x 不存在 抛出异常
list.count(x): 返回指定元素 x 在列表里出现的次数
len(list): 列表长度 返回列表里包含元素的个数

list.reverse(): 反转列表 
list.sort(): 排序 
list.copy(): 浅拷贝

python 列表大小可变



033. 创建列表的 4 种 方式
基本语法创建 [] 

a=[10,20,"Abel","sxt"]
a=[]

>>> a=list() #创建一个空的列表对象
>>> a=[20,30,40,"Abel"]
>>> a[0]
20
>>> a[3]
'Abel'
>>> a=[]  # 创建空列表
>>> a.append(20)
>>> a
[20]


list() 创建
使用 list() 可以将任何迭代的数据转化成列表
a=list()

>>> a=list()
>>> a
[]
>>> a=list("Abel, Eric")
>>> a
['A', 'b', 'e', 'l', ',', ' ', 'E', 'r', 'i', 'c']

>>> range(10)
range(0, 10)
>>> a=range(10)
>>> type(a)
<class 'range'>
>>> # a 不是列表 将 range 转成 列表对象
>>> list(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


通过 range() 创建整数列表
range() 创建整数列表

range([start,]end [,step])

range() 返回的是一个 range 对象 不是列表 需要通过 list() 方法将其转化成列表对象 

>>> range(10)
range(0, 10)
>>> a=range(10)
>>> type(a)
<class 'range'>
>>> # a 不是列表 将 range 转成 列表对象
>>> list(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(3,20,2))
[3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> list(range(20,3,-1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]
>>> list(range(-10,-33,-2))
[-10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32]


推倒式
>>> a=[x*2 for x in range(5)]
>>> a
[0, 2, 4, 6, 8]

>>> a=[x*2 for x in range(100) if x%9==0]
>>> a
[0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]


034. 元素的 5 种 添加方式 效率问题

列表元素的增加和删除 

append() 方法 
>>> a=[20,40]
>>> a.append(80)
>>> a
[20, 40, 80]

>>> a=[20,40]
>>> id(a)
1923134638664
>>> a.append(80)
>>> a
[20, 40, 80]
>>> id(a)
1923134638664
a.append() 方法 不改变 a 地址


+ 运算符操作 
不是真正的尾部添加元素 而是创建新的列表对象 
将原来的列表的元素和新列表元素一次复制到新的列表对象种 
会涉及到大量的复制操作 不建议使用 


>>> a=[20,40]
>>> id(a)
2486252330696
>>> a=a+[50]
>>> id(a)
2486297643272
>>> a
[20, 40, 50]


地址发生变化 创建了 新的列表对象 

# extend() 括号里是列表 不是元素 
# append（） 括号里的是元素  
extend() 
>>> a=[20,40]
>>> id(a)
2486252330696
>>> a.extend([80,90])
>>> id(a)
2486252330696
>>> a
[20, 40, 80, 90]


insert() 
将指定的元素 插入对象的任意位置 

>>> a=[10,20,30,40]
>>> a.insert(2,90)
>>> a
[10, 20, 90, 30, 40]


乘法扩展
>>> a=[90,'sxt']
>>> b=a*3
>>> b
[90, 'sxt', 90, 'sxt', 90, 'sxt']




035. 列表 元素删除的三种方式 
删除的本质是数组元素的拷贝 

>>> a="sxtsxtsxtsxt"
>>> id(a)
1718124182000
>>> a.replace("s","A")
'AxtAxtAxtAxt'
>>> id(a)
1718124182000
>>> a
'sxtsxtsxtsxt'



del 删除 
>>> a=[10,20,30]
>>> del a[1]
>>> a
[10, 30]


pop() 
删除并返回指定位置元素 如果未指定位置 则 默认操作列表的最后一个元素

>>> a=[10,20,30,40,50]
>>> a.pop()
50
>>> a.pop(1)
20
>>> a
[10, 30, 40]


remove() 
删除首次出现的指定元素 如不存在 则抛出异常

>>> a=[10,20,30,40,50,80,90]
>>> a.remove(40)
>>> a
[10, 20, 30, 50, 80, 90]
>>> a.remove(100)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.remove(100)
ValueError: list.remove(x): x not in list

>>> a=["aa","bb","cc","gao","abel","eric"]
>>> a.remove("cc")
>>> a
['aa', 'bb', 'gao', 'abel', 'eric']
>>> a.remove("sdsf")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.remove("sdsf")
ValueError: list.remove(x): x not in list



036. 列表元素的访问和计数

可以通过索引直接访问元素 

>>> a=[10,20,40,60,90]
>>> a[2]
40
>>> a[10]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[10]
IndexError: list index out of range

index() 获得指定元素在列表种首次出现的索引

>>> a=[10,20,30,40,50,60]
>>> a.index(20)
1
>>> a=[10,20,30,40,50,20,45]
>>> a.index(20)
1
>>> a.index(20,3)
5

index(value,[start,[end]])
指定搜索范围 


count() 或者指定元素在列表种出现的次数 
>>> a=[10,20,30,40,20,60,80,90,20]
>>> a.count(20)
3


len() 返回列表长度
>>> a=[10,20,30]
>>> len(a)
3

成员资格的判断

判断列表种是否存在指定的元素 使用 count() 方法 返回 0 表示不存在 
使用 in 关键字来判断 True False 

>>> a=[10,20,30,40,60]
>>> 20 in a
True
>>> 100 not in a
True

>>> a.count(100)>0
False
>>> a.count(99)>0
False


037. 列表 切片操作 slice 

标准格式
[起始偏移量 start： 终止偏移量 end [:步长 step]]

[:]     [10,20,30][:]  
[start:] start    [10,20,30][1:] 
[:end]     [10,20,30][:2]
[start:end]  [10,20,30,40][1:3]
[start:end:step]   [10,20,30,40,50,60,70][1:6:2]


>>> a=[10,20,30,40,60,50]
>>> a[:]
[10, 20, 30, 40, 60, 50]
>>> a[1:3:1]
[20, 30]
>>> a[1::2]
[20, 40, 50]
>>> a[1:]
[20, 30, 40, 60, 50]
>>> a[:2]
[10, 20]


三个量为负数

[10,20,30,40,50,60,70][-3:]
[50, 60, 70]


[10,20,30,40,50,60,70][-5:-3]
[30, 40]


[10,20,30,40,50,60,70][::-1]
[70, 60, 50, 40, 30, 20, 10]


>>> a=[10,20,30,40]
>>> a[1,100]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[1,100]
TypeError: list indices must be integers or slices, not tuple
>>> a[1:100]
[20, 30, 40]

列表遍历
>>> for x in a:
	print(x)

	
10
20
30
40


038. 列表 排序 a.reverse() 逆序 

>>> a=[20,10,40,30,60]
>>> id(a)
2402218920008
>>> a.sort()
>>> a
[10, 20, 30, 40, 60]
>>> id(a)
2402218920008
>>> a.sort(reverse=True)
>>> a
[60, 40, 30, 20, 10]


>>> a=[10,90,80,60]
>>> a
[10, 90, 80, 60]
>>> id(a)
2544175390088
>>> a.sort()
>>> a
[10, 60, 80, 90]
>>> id(a)
2544175390088
>>> a.sort(reverse=True)
>>> a
[90, 80, 60, 10]
>>> id(a)
2544175390088

# a.sort() a.sort(reverse=True)  操作 不改变 a 的地址 
# 但是列表里 元素的顺序发生了变化 永久改变元素在列表中的位置 list.sort() 


随机排序
>>> import random
>>> random.shuffle(a)
>>> a
[20, 60, 40, 30, 10]




建新列表的排序 
生成新的列表对象

>>> a=[20,10,90,80,60,50]
>>> a
[20, 10, 90, 80, 60, 50]
>>> id(a)
1790270031560
>>> b=sorted(a)
>>> b
[10, 20, 50, 60, 80, 90]
>>> id(b)
1790270260872
>>> c=sorted(a,reverse=True)
>>> c
[90, 80, 60, 50, 20, 10]
>>> id(c)
1790269998344
>>> id(a)
1790270031560



reversed() 返回迭代器
需要返回一个逆序的排列 

reversed()  不对原列表做任何修改 只是返回一个逆序排列的迭代器对象
迭代器只能用一次

>>> a=[20,10,30,60,90,80]
>>> a[::-1]
[80, 90, 60, 30, 10, 20]
>>> a
[20, 10, 30, 60, 90, 80]
>>> c=reversed(a)
>>> c
<list_reverseiterator object at 0x00000289F2EB75C0>
>>> list(c)
[80, 90, 60, 30, 10, 20]
>>> list(c)
[]

max 和 min sum 

sum 对数值型的列表有用  其他的不适用


>>> a=[20,10,30,60,90,80]
>>> a[::-1]
[80, 90, 60, 30, 10, 20]
>>> a
[20, 10, 30, 60, 90, 80]
>>> c=reversed(a)
>>> c
<list_reverseiterator object at 0x00000289F2EB75C0>
>>> list(c)
[80, 90, 60, 30, 10, 20]
>>> list(c)
[]
>>> a=[3,10,20,15,9]
>>> max(a)
20
>>> min(a)
3
>>> sum(a)
57



039. 列表 二位列表 表格数据的存储和 提取 

>>> a=[
	["Abel-1",18,30000,"Beijing"],
	["Abel-2",19,30000,"Shanghai"],
	["Eriuc",20,100000,"Shenzheng"]
	]
>>> a
[['Abel-1', 18, 30000, 'Beijing'], ['Abel-2', 19, 30000, 'Shanghai'], ['Eriuc', 20, 100000, 'Shenzheng']]

>>> a[0]
['Abel-1', 18, 30000, 'Beijing']
>>> a[0][1]
18
>>> a[0][3]
'Beijing'

>>> for m in range(3):
	for n in range(4):
		print(a[m][n],end="\t")
	print()

	
Abel-1	18	30000	Beijing	
Abel-2	19	30000	Shanghai	
Eriuc	20	100000	Shenzheng



040. 元组 特点 tuple 创建的两种方式
列表属于可变序列， 可以任意修改列表的元素 
元组属于不可变序列 不能修改元组中的元素 
元组 没有 增加 修改 删除相关的方法 

只需要学习 
元组的 创建 删除 元素的访问 计数 
元组支持的操作：
1. 索引访问
2. 切片操作
3. 连接操作 
4. 成员关系操作 
5. 比较运算操作
6. 计数： 元组的长度 最大值 最小值 求和 
		len()   max()   min()  sum() 
		
		
元组的创建 
>>> a=(10,20,30)
>>> type(a)
<class 'tuple'>
>>> b=(20,)
>>> type(b)
<class 'tuple'>
>>> a
(10, 20, 30)
>>> b
(20,)
>>> c=tuple()
>>> c
()
>>> b=tuple("abc")
>>> b
('a', 'b', 'c')
>>> b=list("abcd")
>>> b
['a', 'b', 'c', 'd']
>>> b=tuple(range(3))
>>> b
(0, 1, 2)
>>> b=tuple([30,40,50])
>>> b
(30, 40, 50)

>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b
NameError: name 'b' is not defined



041. 元组 元素的访问 计数方法 
1. 元组的元素不能修改 

>>> a=(20,30,40)
>>> a[0]
20
>>> a[1]=90
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a[1]=90
TypeError: 'tuple' object does not support item assignment
>>> a=tuple("abcdefghijklmnopqrstuvwxyz")
>>> a
('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
>>> a[1:10]
('b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
>>> a[::-1]
('z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')


列表排序的方法 list.sort() 是修改列表对象 元组没有该方法 
如果要对元组排序 只能 使用 内置函数 sorted(tupleObj) 
并生成新的 列表 对象  注意 这里 生成的是列表对象 

# 内置函数 sorted(元组) 得到 列表  important 
>>> b=(20,30,90,10)
>>> sorted(b)
[10, 20, 30, 90]

>>> a=1,20
>>> b=30,40
>>> a+b
(1, 20, 30, 40)

拼接完以后 也是元组 

>>> len(a)
2
>>> sum(a)
21
>>> max(a)
20
>>> min(a)
1


zip 
将多个列表对应位置的元素组合称为元组 并返回这个 zip 对象 
 
>>> a=[10,20,30]
>>> b=[40,50,60]
>>> c=[70,80,90]
>>> d=zip(a,b,c)
>>> list(d)
[(10, 40, 70), (20, 50, 80), (30, 60, 90)]
>>> d
<zip object at 0x000001388FFC8548>




042. 元组 生成器推倒式 创建元组
>>> s=(x*2 for x in range(5))
>>> s
<generator object <genexpr> at 0x000001388FFF3D00>
>>> tuple(s)
(0, 2, 4, 6, 8)
>>> tuple(s)
()


>>> s=(x*2 for x in range(5))
>>> s.__next__()
0
>>> s.__next__()
2
>>> s.__next__()
4
>>> s.__next__()
6
>>> s.__next__()
8
>>> s.__next__()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.__next__()
StopIteration


元组总结 
元组是 不可变序列
元组的访问和处理速度比列表快 
与整数和字符串一样 元组可以作为字典的键 列表则永远不能作为字典的键使用




043. 字典 特点 4 种 创建方式
字典是 键值对  的无序可变序列 
字典种的每一个元素都是 一个 键值对 包含 键对象 值对象
可以通过 键对象 实现快速 获取 删除 更新对应的  值对象 

键 是任意不可变数据  整数 浮点数 字符串 元组 
		列表 字典 集合 是可变对象 不能作为 键
值 是任意的数据 可重复 


字典的创建 
1. 使用 {} dict() 来创建字典对象  
a={'name':'Eric','age':18,'job':'programmer'}

>>> a={"name":"Eric","age":18,"job":"Programmer","dd":[2,3,4]}
>>> a
{'name': 'Eric', 'age': 18, 'job': 'Programmer', 'dd': [2, 3, 4]}


>>> b=dict(name='Eric',age=18,job='Programmer')

>>> c=dict([("name","Eric"),("age",18)])
>>> c
{'name': 'Eric', 'age': 18}

# 创建空的字典对象
>>> a={}
>>> d=dict()


2. 通过 zip() 创建字典对象
>>> k=['name','age','job']
>>> v=['eric',18,'student']
>>> d=dict(zip(k,v))
>>> d
{'name': 'eric', 'age': 18, 'job': 'student'}



3. 通过 fromkeys 创建值为空的字典 
>>> a=dict.fromkeys(['name','age','job'])
>>> a
{'name': None, 'age': None, 'job': None}




044. 字典元素的访问  键的访问 值的访问

>>> a={"name":"Eric","age":18,"job":"Programmer"}
>>> a
{'name': 'Eric', 'age': 18, 'job': 'Programmer'}
>>> a["name"]
'Eric'
>>> a['dd']
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a['dd']
KeyError: 'dd'
>>> a.get("name")
'Eric'
>>> a.get("xxx")
>>> print(a.get("xxx"))
None
>>> a.get("ddd","不存在")
'不存在'


列出 所有的 键值对 

>>> a={"name":"Eric","age":18,"job":"Programmer"}
>>> a
{'name': 'Eric', 'age': 18, 'job': 'Programmer'}
>>> a.items()
dict_items([('name', 'Eric'), ('age', 18), ('job', 'Programmer')])
>>> a.keys()
dict_keys(['name', 'age', 'job'])
>>> a.values()
dict_values(['Eric', 18, 'Programmer'])
>>> len(a)
3
>>> "name" in a
True


045. 字典元素的 添加 修改  删除

>>> a={"name":"Eric","age":18,"job":"Programmer"}
>>> a["address"]="280W renner road"
>>> a
{'name': 'Eric', 'age': 18, 'job': 'Programmer', 'address': '280W renner road'}

如果 键 已经存在 则覆盖旧的键值
 
>>> a["name"]="Abel"
>>> a
{'name': 'Abel', 'age': 18, 'job': 'Programmer', 'address': '280W renner road'}


2. 使用 update() 将新字典中所有的键值 全部添加到旧字典对象上 如果 key 有重复， 则直接覆盖 

>>> b={"name":"Eric","salary":10000,"sex":"female"}
>>> a.update(b)
>>> a
{'name': 'Eric', 'age': 18, 'job': 'Programmer', 'address': '280W renner road', 'salary': 10000, 'sex': 'female'}

3. 字典中 元素的删除 可以使用 del() 方法 ， 或者 clear() 删除所有的键值对 ， pop() 指定删除 键值对， 并返回相应的值对象 


>>> del(a["age"])
>>> a
{'name': 'Eric', 'job': 'Programmer', 'address': '280W renner road', 'salary': 10000, 'sex': 'female'}
>>> b=a.pop("name")
>>> b
'Eric'
>>> a
{'job': 'Programmer', 'address': '280W renner road', 'salary': 10000, 'sex': 'female'}
>>> a.clear()
>>> a
{}


popitem() : 随机删除并返回键值对 
字典是 “无序可变序列”  因此没有第一个 最后一个 元素的概念 如想一个接着一个移除并处理项， 这个方法就很有效 

>>> a={"name":"Eric","age":18,"job":"Programmer"}
>>> a.popitem()
('job', 'Programmer')
>>> a
{'name': 'Eric', 'age': 18}
>>> a.popitem()
('age', 18)
>>> a
{'name': 'Eric'}
>>> a.popitem()
('name', 'Eric')
>>> a
{}


046. 字典 序列解包用于列表元组 
序列解包 可以用于 元组 列表 字典 
序列解包 可以方便对多个变量赋值 

>>> [x,y,z]=[10,20,30]
>>> x
10
>>> y
20
>>> z
30


>>> x,y,z=(20,30,10)
>>> x
20
>>> y
30
>>> z
10
>>> (a,b,c)=(10,20,30)
>>> a
10
>>> b
20
>>> c
30

>>> x,y,z=10,20,30
>>> x
10
>>> y
20
>>> z
30


>>> s=dict(name="eric",age=18,job="Programmer")
>>> s
{'name': 'eric', 'age': 18, 'job': 'Programmer'}
>>> a,b,c=s
>>> a
'name'
>>> b
'age'
>>> c
'job'
>>> e,d,f=s.values()
>>> e
'eric'
>>> d
18
>>> f
'Programmer'
>>> h,i,j=s.items()
>>> h
('name', 'eric')
>>> i
('age', 18)
>>> j
('job', 'Programmer')

>>> h[0]
'name'
>>> h[1]
'eric'

047. 复杂表格数据存储
>>> r1={"name":"Eric","age":18,"city":"Beijing"}
>>> r2={"name":"Abel","age":20,"city":"Beijing- changping"}
>>> r3={"name":"Ana","age":19,"city":"Shanghai"}
>>> tb=[r1,r2,r3]
>>> tb
[{'name': 'Eric', 'age': 18, 'city': 'Beijing'}, {'name': 'Abel', 'age': 20, 'city': 'Beijing- changping'}, {'name': 'Ana', 'age': 19, 'city': 'Shanghai'}]
>>> #获得第二行 薪资
>>> print(tb[1].get("age"))
20


>>> for i in range(len(tb)):
	print(tb[i].get("age"))

	
18
20
19


>>> for i in range(len(tb)):
	print(tb[i].get("name"),tb[i].get("age"),tb[i].get("city"))

	
Eric 18 Beijing
Abel 20 Beijing- changping
Ana 19 Shanghai


048. 字典 核心底层原理

049. 字典 

050. 集合 特点 创建 删除 交集 并集
集合是无序可变 元素不能重复  

集合创建和删除

>>> a={233,2,30,"gg"}
>>> a
{233, 2, 30, 'gg'}
>>> a.add(30)
>>> a
{233, 2, 30, 'gg'}
>>> a.add(90)
>>> a
{2, 'gg', 233, 90, 30}


>>> a=list("abcd")
>>> a
['a', 'b', 'c', 'd']
>>> b=set(a)
>>> b
{'c', 'a', 'd', 'b'}

>>> a={10,20,30,40}
>>> a.remove(40)
>>> a
{10, 20, 30}
>>> a.clear()
>>> a
set()


集合的相关操作 

>>> a={1,3,'sxt'}
>>> b={'he','it','sxt'}
>>> #并集
>>> a|b
{1, 'sxt', 3, 'it', 'he'}
>>> #交集
>>> a&b
{'sxt'}
>>> #差集
>>> a-b
{1, 3}


>>> a.union(b)
{1, 'sxt', 3, 'it', 'he'}
>>> a.intersection(b)
{'sxt'}
>>> a.difference(b)
{1, 3}



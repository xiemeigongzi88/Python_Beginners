第三章  列表简介
Page 26 - 33 

Page 26 
3.1 列表是 什么？

列表： 
	由一系列按照 特定顺序排列的元素组成 
	其中元素之间可以没有任何关系 
用 [] 来表示列表 

bicycles=['trek','cannondale','redline','specialized']
print(bicycles)


OUT：
['trek', 'cannondale', 'redline', 'specialized']


3.1.1 访问列表元素 
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0])

OUT：
trek

######################################
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0].title())


OUT：
Trek


########################################
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[1])
print(bicycles[3])
print("###########")
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])

OUT：
cannondale
specialized
###########
specialized
redline
cannondale
trek



3.1.3 使用列表中的各个值
可以使用拼接根据列表中的值 来 创建信息 

bicycles=['trek','cannondale','redline','specialized']
message="My first bicycle was a "+bicycles[0].title()+"."
print(message)

OUT：
My first bicycle was a Trek.


###########################################

EXC 3-1 
names=['Abel','Erica','Eric','Batholomew','Ana','Ada']
print(names)
for i in range(len(names)):
    print(names[i])


OUT：
['Abel', 'Erica', 'Eric', 'Batholomew', 'Ana', 'Ada']
Abel
Erica
Eric
Batholomew
Ana
Ada


#######################################
EXC  3-2
names=['Abel','Erica','Eric','Batholomew','Ana','Ada']
print(names)
for i in range(len(names)):
    print(names[i]+"\n   Good Luck!")
    

################
EXC  3-3 


Page 27 

3.2 修改 添加 删除 元素
创建的 列表是动态的 在列表创建后 可与运行 删除 增加 操作 
	
3.2.1 修改列表元素 
motor=['honda','yamaha','suzuki']
print(motor)

motor[2]='ducati'
print(motor)

OUT：
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'ducati']



motor[3]='scar'
   
IndexError: list assignment index out of range
## 也就是说 列表只能对已存在的元素进行修改 


3.2.2 在列表中添加元素 
1. 在列表末尾添加元素 

motor=['honda','yamaha','suzuki']
print(motor)

motor.append('ducati')
print(motor)

OUT：
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']


##################################

a=[]
print(a)

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)

print(a)

OUT：
[]
[1, 2, 3, 4, 5, 6]

经常要等到程序运行后 才能知道 用户在程序中存储了哪些数据 


2. 在列表中插入元素 
使用 insert() 方法 可在任意为止添加新元素 

a=['honda','toyota','Benz','LandRover','nissa']
print(a)
a.insert(1,'civic')
print(a)

OUT:
['honda', 'toyota', 'Benz', 'LandRover', 'nissa']
['honda', 'civic', 'toyota', 'Benz', 'LandRover', 'nissa']


3.2.3 从列表中删除元素 
1. 使用 del 语句删除元素 

a=['honda','toyota','Benz','LandRover','nissa']
print(a)

del a[4]
print(a)

OUT：
['honda', 'toyota', 'Benz', 'LandRover', 'nissa']
['honda', 'toyota', 'Benz', 'LandRover']




2. 使用 pop() 方法 删除元素 
将元素从列表中删除 并接着使用这个元素的值

pop() 可以删除列表末尾的元素 并可以使用 

a=['honda','toyota','Benz','LandRover','nissa']
print(a)

b=a.pop()
print(b)
print(a)

OUT：

['honda', 'toyota', 'Benz', 'LandRover', 'nissa']
nissa
['honda', 'toyota', 'Benz', 'LandRover']

##################################
a=['honda','toyota','Benz','LandRover','nissa']

b=a.pop()

print("The last motor I owned was a "+b.title()+".")

OUT：
The last motor I owned was a Nissa.


3. 弹出列表中任意位置的元素 
a=['honda','toyota','Benz','LandRover','nissa']
print(a)

b=a.pop(0)
print(b)
print(a)

OUT：
['honda', 'toyota', 'Benz', 'LandRover', 'nissa']
honda
['toyota', 'Benz', 'LandRover', 'nissa']

当使用 pop() 时， 被弹出的元素就不在列表中了 
如果要从列表中删除一个元素 且 不再以任何方式使用， 就是用 del 语句
如果要在删除元素后还要再使用它， 就使用 pop() 方法 


4. 根据值 删除元素 
不知道 从列表中删除的值 所在的位置 
使用 remove() 方法  

a=['honda','toyota','Benz','LandRover','nissa']
print(a)

a.remove('Benz')
print(a)


OUT：
['honda', 'toyota', 'Benz', 'LandRover', 'nissa']
['honda', 'toyota', 'LandRover', 'nissa']


使用 remove() 从列表中删除元素时， 也课接着使用它的值 

a=['honda','toyota','benz','LandRover','nissa']
print(a)

b='benz'
a.remove(b)
print(a)

print("\nA "+b.title()+" is too expensive for me.")

OUT：
['honda', 'toyota', 'benz', 'LandRover', 'nissa']
['honda', 'toyota', 'LandRover', 'nissa']

A Benz is too expensive for me.


OUT：
['honda', 'toyota', 'benz', 'LandRover', 'nissa']
['honda', 'toyota', 'LandRover', 'nissa']

A Benz is too expensive for me.

Note:
方法 remove() 只是删除第一个指定的值， 如果要删除 的值可能在列表中出现多次 就需要循环来判断是否删除了所有这样的值

remove() 根据元素的内容删除 
pop() 根据元素的位置删除 


Page 30
3.3 组织列表
3.3.1 使用方法 sort() 对列表进行永久性排序 
对列表元素排列顺序的修改是 永久性的 

cars=['bmw','audi','toyota','subaru']
print(cars)

cars.sort()
print(cars)


OUT：
['bmw', 'audi', 'toyota', 'subaru']
['audi', 'bmw', 'subaru', 'toyota']

# 永久性地修改了列表元素地顺序 再也无法恢复到 原来的排列顺序 

还可以按与字母顺序相反的顺序排列列表元素 


cars=['bmw','audi','toyota','subaru']
print(cars)

cars.sort()
print(cars)


cars.sort(reverse=True)
print(cars)

OUT：
['bmw', 'audi', 'toyota', 'subaru']
['audi', 'bmw', 'subaru', 'toyota']
['toyota', 'subaru', 'bmw', 'audi']



3.3.2 使用函数 sorted() 对列表进行临时排序 
	要保留 原来 列表元素的排列顺序， 同时能以特定的顺序呈现列表元素， 可是使用 sorted() 函数 
	
sorted() 能够按照特定的顺序显示 列表元素 同时不影响它们在列表中的原始排列顺序 


cars=['bmw','audi','toyota','subaru']
print("here is the original list:")
print(cars)

print("\nhere is the sorted list:")
print(sorted(cars))

print("\nhere is the original list again:")
print(cars)


OUT：
here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']

调用 函数 sorted() 以后， 列表元素的排列顺序没有发生改变 

print("\nhere is the reverse sorted list:")
print(sorted(cars,reverse=True))

OUT：
here is the reverse sorted list:
['toyota', 'subaru', 'bmw', 'audi']


3.3.3 倒着打印列表
要反转列表元素的排列顺序 可以使用 reverse() 

cars=['bmw','audi','toyota','subaru']

print(cars)

cars.reverse()
print(cars)

OUT：
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']

##Note:
方法 reverse() 永久的修改了 列表元素的排列顺序， 但是可以随时恢复到原来的排列顺序 只需要 对列表再次调用 reverse() 即可 


3.3.4 确定列表的长度
len()  

>>> cars=['bmw','audi','toyota','subaru']
>>> len(cars)
4



Page  32 
3.4 使用列表时 避免索引错误 

 cars=['bmw','audi','toyota','subaru']

print(cars[4])

OUT：
IndexError: list index out of range

####################################


cars=['bmw','audi','toyota','subaru']

print(cars[-1])

a=[]
print(a[-1])

OUT：
subaru

  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 6, in <module>
    print(a[-1])
IndexError: list index out of range

#Note：
仅当列表未空的时候，不包含任何元素 


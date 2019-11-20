第二章 变量和简单数据类型

Page 18 

2.1 运行 hello_world 时 发生的情况


2.2 变量
#2.2 variable
#2.2.1
message="Hello World ！"
print(message)

message="Hello World Crash Course World!"
print(message)

Hello World ！
Hello World Crash Course World!



2.2.1 变量的命名和使用 
1. 变量名 只能包含字母 数字 下划线 
	变量名 可以 字母 或者 下划线 开头 但是不能用数字开头
2.  变量名 不能包含空格 但是可以用下划线 来分割其中的单词
3. 不能用 关键字 和 函数名用作变量名 


2.2.2 使用变量时避免命名错误 
 
>>> message="Hello Python!"
>>> print(masage)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(masage)
NameError: name 'masage' is not defined



Page 20 
2.3 字符串

2.3.1 使用方法修改字符串的大小写 
>>> name="ada lovelace"
>>> print(name.title())
Ada Lovelace

函数 title() 不需要额外的信息 所以括号是空的 

title() 以 首字母 大写的 方式显示每个单词 即将每个单词的首字母改为大写 


>>> name="ada lovelace"
>>> print(name.title())
Ada Lovelace
>>> name="Ada Lovelace"
>>> print(name.upper())
ADA LOVELACE
>>> print(name.lower())
ada lovelace


2.3.2 合并（拼接）字符串
first_name="ada"
last_name="lovelace"

full_name=first_name+" "+last_name

print(full_name)

OUT：
ada lovelace

#####################################
first_name="ada"
last_name="lovelace"

full_name=first_name+" "+last_name

print("Hello, "+full_name.title()+" !")

OUT:
Hello, Ada Lovelace !

########################################
first_name="ada"
last_name="lovelace"

full_name=first_name+" "+last_name

message="Merry Christmas，Mr. "+full_name.title()+" !"

print(message)

OUT：
Merry Christmas，Mr. Ada Lovelace !



2.3.3 使用 制表符 或者 换行符 来添加空白 
	空白： 泛指 任何非打印字符： 如 空格 制表符 换行符 

制表符： \t
print("python")
print()
print("\tPython")

OUT：
python

	Python
	
换行符： \n 

print("Language:\nPython\n C \n Java")

OUT:
Language:
Python
 C 
 Java
 
同一个字符串中 同时 包含 制表符 和 换行符 

print("Language:\n\tPython\n\tC\n\t Java")

OUT：
Language:
	Python
	C
	 Java
	 
	 
Page 21 
2.3.4 删除空白 
python 能够找出字符串 开头 和 末尾 多余的空白 确保字符串没有空白 

>>> a="python     "
>>> a
'python     '
>>> a.rstrip()
'python'
>>> a
'python     '

这种删除只是暂时的 下次再次访问 a 的时候， a 没有发生变化 
# 新建了一个新的对象 




lstrip() && strip()

>>> b="    python    "
>>> b
'    python    '
>>> b.lstrip()
'python    '
>>> b.strip()
'python'
>>> b
'    python    '




2.3.5 使用字符串时 避免语法错误 

在用 单引号 括起来的 字符串中， 如果包含撇号 就将导致错误 

message= "One of Python's strengths is its diverse community."
print(message)

a='One of Python's strengths is its diverse community.'
print(a)

OUT：
  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 4
    a='One of Python's strengths is its diverse community.'
                     ^
SyntaxError: invalid syntax

撇号 位于 两个 双引号之间 Python 解释器 能够正确理解 这个字符串



2.3.6 Python 2 中的 print 语句 


Page 22 
2.4 数字 

2.4.1 整数
# 空格 不影响 Python 计算表达式 的 方式 
>>> 2+3
5
>>> 3-2
1
>>> 2*3
6
>>> 3/2
1.5
>>> 3**2
9
>>> 3**3
27
>>> 10**6
1000000


>>> (2+3)*4
20
>>> 2+3*4
14


2.4.2 浮点数 
>>> 0.1+0.1
0.2
>>> 0.2+0.2
0.4
>>> 2*0.1
0.2
>>> 0.1*2
0.2
>>> 0.2+0.1
0.30000000000000004
>>> 3*0.1
0.30000000000000004


2.4.3 使用函数 str() 避免类型错误
 
age=23
message="Happy"+age+"rd Birthday!"
print(message)

OUT:
Traceback (most recent call last):
  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 2, in <module>
    message="Happy"+age+"rd Birthday!"
TypeError: must be str, not int

#############################
age=23
message="Happy "+str(age)+"rd Birthday!"
print(message)

OUT:
Happy 23rd Birthday!


2.5 注释 


2.6 Python 之禅
import this 

############################################
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

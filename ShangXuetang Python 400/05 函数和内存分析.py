05 函数和内存分析 
067- 085 

067. 函数的基本概念 内存分析 函数的分类 

def  函数名([形参列表])
#	'''文档字符串'''
	
	函数体/若干语句
	
	
068. 形参 和 实参  文档字符串

def printMax(a,b):
    if(a>b):
        print(a)
    else:
        print(b)

printMax(10,20)
printMax(200,300)



打印文档字符串:
	help(函数名，__doc__) 
	
	
	
	def print_star(n):
    '''print the stars in doc'''
    print("******")


help(print_star)

OUT：
	print_star(n)
    print the stars in doc
	
	
	
069. 函数的返回值 

def average(a,b):
	return (a+b)/2
	
c=average(20,30)
print(c)


def add(a,b):
    print("the sum of two numbers:{0}+{1}={2}".format(a,b,a+b))
    return a+b

c=add(1,2)
print(c)
print(add(1,3)*4)

OUT:
the sum of two numbers:1+2=3
3
the sum of two numbers:1+3=4
16


包含 return 结束函数执行 并返回值 

函数体不 包含 return 语句 返回 None 
需要返回多个

返回多个值：

def test03(x,y,z):
	return [x*10,y*10,z*10]
	
print(test03(1,2,3))


070. 函数也是对象 内存的底层分析 
def test01():
    print("sxt")

test01()

c=test01
c()

print(id(c))
print(id(test01))


OUT：
sxt
sxt
1296583461608
1296583461608


071. 变量的作用域 全局变量 局部变量 


a=100 #全局变量

def test01():
	global a #如果在函数内 改变全局变量的值 增加 global 关键字
	print(a) #打印全局变量
	
	a=300
	
	
	
test01()
print(a)

#########################

a=3

def test01():
    b=4
    print(b*2)
 #   print(a) #报错 局部变量a 引用前 必须赋值

    global a
    a=300
    print(a)
    print(locals())
    print(globals())

test01()

print(a)

#print(b)

OUT：
8
300
{'b': 4}
{'__builtins__': {'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <bound method ImportHookManager.do_import of <module '_pydev_bundle.pydev_import_hook.import_hook'>>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'WindowsError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'BufferError': <class 'BufferError'>, 'MemoryError': <class 'MemoryError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-Z plus Return to exit, 'exit': Use exit() or Ctrl-Z plus Return to exit, 'copyright': Copyright (c) 2001-2017 Python Software Foundation.
All Rights Reserved.



072. 局部变量 和 全局变量 效率的测试

import math 
import time 

def test01():
	start=time.time()
	for i in range(10000000):
		math.sqrt(30)
	
	end =time.time()
	print(end-start)
	
def test02():
	b=math.sqrt
	start=time.time()
	for i in range(1000000):
		b(30)
	end=time.time()
	print(end-start)

	
test01()
test02()

1.5408358573913574
0.10911107063293457


073. 参数的传递
参数传递为 引用传递 不是值传递 
1. 对 可变对象 进行 写操作 直接作用域原来的对象
2. 对不可变 对象 进行 写操作 产生新的 对象空间 并用新的值 填充这个空间 

可变对象：
	字典 列表 集合  自定义对象 
	
不可变对象：
	数字 字符串 元组 function
	
	
传递可变对象的引用

b=[10,20]

def f2(m):
	print("m:".id(m))
	m.append(30)
	
	
f2(b)
print("b:".id(b))
print(b)

####################################
b = [10, 20]

def f2(m):
    print(id(m))
    m.append(30)

f2(b)
print(id(b))
print(b)

OUT：
2517016533832
2517016533832
[10, 20, 30]


074. 传递不可变对象

数字 字符串 元组 布尔值 
实际传递的还是一个对象的引用 在赋值操作的时候， 由于不可变对象无法修改
系统会新创建一个对象

a=100
def f1(n):
	print("id(n):",id(n))
	n+=200
	print("id(n):",id(n))
	print(n)
	
f1(a)
print("id(a):",id(a))
print(a)

OUT:
id(n): 1921150208
id(n): 2413163745040
300
id(a): 1921150208
100




075. 浅拷贝和深拷贝  内存分析 
copy()   deepcopy()

浅拷贝： 不拷贝子对象的内容 只是拷贝子对象的引用
深拷贝： 会连子对象的内存也拷贝一份 对子对象的修改不会影响对象


id(n): 1921150208
id(n): 2413163745040
300
id(a): 1921150208

a: [10, 20, [5, 6]]
b: [10, 20, [5, 6]]
浅拷贝
a: [10, 20, [5, 6, 7]]
b: [10, 20, [5, 6, 7], 30]


############################
import copy
a=[10,20,[5,6]]
b=copy.copy(a)

print("a:",a)
print("b:",b)

b.append(30)
b[2].append(7)

print("浅拷贝")

print("a:",a)
print("b:",b)

OUT：
a: [10, 20, [5, 6]]
b: [10, 20, [5, 6]]
浅拷贝
a: [10, 20, [5, 6, 7]]
b: [10, 20, [5, 6, 7], 30]


#########################

import copy

a=[10,20,[5,6]]
b=copy.deepcopy(a)

print("a:",a)
print("b:",b)

b.append(30)
b[2].append(7)

print("深拷贝")

print("a:",a)
print("b:",b)

OUT：
a: [10, 20, [5, 6]]
b: [10, 20, [5, 6]]
深拷贝
a: [10, 20, [5, 6]]
b: [10, 20, [5, 6, 7], 30]


076. 参数的传递 不可变对象 含 可变子列

#传递不可变对象时 如果发生赋值操作 用的是 浅拷贝 


a=0
print("a",id(a))

def test01(m):
    print("m:",id(m))
    m=20
    print(m)
    print("m:",id(m))

test01(a)

OUT:
a 1482580096
m: 1482580096
20
m: 1482580736


##########################
a = (10, 20, [5, 6])
print("a:", id(a))


def test01(m):
    print("m:", id(m))
    m[2][0] = 888
    print(m)
    print("m:", id(m))


test01(a)
print(a)


OUT:
a: 1527744892792
m: 1527744892792
(10, 20, [888, 6])
m: 1527744892792
(10, 20, [888, 6])

传递不可变对象的时候， 不可变对象里面包含的子对象时可变的 
则 方法内 修改了这个可变对象 源对象也发生了变化 


a = (10, 20, [5, 6])
print("a:", id(a))


def test01(m):
    print("m:", id(m))
    m[2][0] = 888
    print(m)
    print("m:", id(m))


test01(a)
print(a)


OUT:
a: 1527744892792
m: 1527744892792
(10, 20, [888, 6])
m: 1527744892792
(10, 20, [888, 6])


#####################
a=(10,20,[80,90])
print(id(a))

def test01(m):
    print("m:",id(m))
    m[2][0]=88
    print(m)
    print("m:",id(m))
    m[2][2]=98
    print(m)
    print("m:", id(m))

test01(a)

OUT：
    m[2][2]=98
IndexError: list assignment index out of range

077. 参数的类型 位置参数 默认值参数

位置参数
def f1(a,b,c)
	print(a,b,c)
	
f1(2,3,4)


默认值参数
必须位于 其他参数的后面 

def f1(a,b,c=10, d=20)
	print(a,b,c,d)
	
f1(8,9)
f1(8,9,19)
f1(8,9,10,20)

#####################
def f1(a,b,c=8,d=9):
    print(a,b,c,d)

f1(1,2)
f1(1,2,3)
f1(1,2,3,4)

OUT:
1 2 8 9
1 2 3 9
1 2 3 4


命名参数
def f1(a,b,c):
        print(a,b,c)

f1(8,9,19)
f1(c=10,a=20,b=30)

OUT：
8 9 19
20 30 10

078. 可变参数：
*  元组 
** 字典

可变参数

def f1(a,b,*c):
    print(a,b,c)

f1(8,9,10,11,12)


def f2(a,b,**c):
    print(a,b,c)

f2(1,2,name="Abel",age=18)

def f3(a,*b,**c):
    print(a,b,c)

f3(1,9,20,16,name="Abel",age=18)


OUT:
8 9 (10, 11, 12)
1 2 {'name': 'Abel', 'age': 18}
1 (9, 20, 16) {'name': 'Abel', 'age': 18}
 

强制明明参数 
def f1(*a,b,c):
    print(a,b,c)

f1(2,7,8,9,b=3,c=4)

OUT：
(2, 7, 8, 9) 3 4





079  lambda 表达式和匿名函数
lambda 函数 实际 生成一个函数 对象 

只允许包含一个表达式 不能包含复杂的语句 
表达式的计算结果就是 函数的返回值 

lambda 基本语法：
	lambda arg1,arg2,arg3,...:<表达式>
	
	
f=lambda a,b,c: a+b+c
print(f)
print(f(2,3,4))

OUT：
<function <lambda> at 0x000002CEF83A2E18>
9


g=[lambda a:a*2, lambda b:b*3, lambda c:c*4]
print(g[0](6),g[1](7),g[2](8))

def test01(a,b,c,d):
    return a*b*c*d

h=[test01,test01]
print(h[0](3,4,5,6))
print(h[1](4,5,6,7))


OUT：
<function <lambda> at 0x000002664FDE1D08>
9
12 21 32
360
840


	
	
080. eval() 函数
将字符串 str 当成有效的表达式来求值 并返回计算结果
语法：
	eval(source[,globals[,locals]])->value 
	

##############################################	
s="print('abcde')"

eval(s)

a=10
b=20
c=eval("a+b")
print(c)

##################

dict1=dict(a=100,b=200)
d=eval("a+b")
print(d)

dict2=dict(a=100,b=200)
d1=eval("a+b",dict1)
print(d1)
	
OUT:
abcde
30
30
300


081. 递归函数 



def test01():
    print("test01()")
    test02()

def test02():
    print("test02()")
    test01()

test01()



##################
def test01(n):
    print("test01:",n)

    if(n==0):
        print("over")
    else:
        test01(n-1)

test01(3)

OUT：
test01: 3
test01: 2
test01: 1


#################################
def test01(n):
    print("test01:",n)

    if(n==0):
        print("over")
    else:
        test01(n-1)

    print("test01***",n)



test01(3)

OUT：
test01: 3
test01: 2
test01: 1
test01: 0
over
test01*** 0
test01*** 1
test01*** 2
test01*** 3



082. 递归函数 计算阶乘 
def functional(n):
    if n==1 :
        return 1
    else:
        return n*functional(n-1)

a=functional(5)
print(a)


083. 嵌套函数

也叫 内部函数 
def outer():
    print("outer running")

    def inner():
        print("inner running")

    inner()

outer()
inner()

OUT：
NameError: name 'inner' is not defined
outer running
inner running


##################################
def printName(isChinese,name,lastName):

    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if isChinese:
        inner_print(lastName,name)
    else:
        inner_print(name,lastName)

printName(True,"歌","英")
printName(False,"Eric","Wong")

OUT：
英 歌
Eric Wong

085. nonlocal 关键字 

def outer():
    b=10

    def inner():
    #    nonlocal b #声明外部函数的局部变量
        print("inner:",b)
    #    b=20

    inner()

outer()

OUT：
inner: 10

############################
def outer():
    b=10

    def inner():
        nonlocal b #声明外部函数的局部变量
        print("inner b:",b)
        b=20

    inner()
    print("outer b:",b)

outer()

OUT：
inner b: 10
outer b: 20


085. LEGB 规则：
查找规则：
Local Enclosed Global Built-in

str="global"

def outer():

    str="outer"
    def inner():
        str="inner"

        print(str)

    inner()
    print(str)


outer()
print(str)


OUT：
inner
outer
global


#####################################









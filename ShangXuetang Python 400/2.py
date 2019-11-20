2.内置数据类型 
009-050

009. 程序的构成

行连接符：
a="adhencjdknecjkecj"
b="frjenfjrkenf\
mvlkfdmv\
vgf"

print(b)
#这个没有结果出来 
SyntaxError: multiple statements found while compiling a single statement


010. 对象的基本组成和内存示意图

>>> a=3
>>> id(3)
1574133984
>>> id(a)
1574133984
>>> 


>>> a=3
>>> a
3
>>> id(3)
1501126880
>>> type(3)
<class 'int'>
>>> 
>>> b="I Love you"
>>> b
'I Love you'
>>> id(b)
2337160974000
>>> type(b)
<class 'str'>
>>> 

>>> b="I love you"
>>> id(b)
2631727440048
>>> id("I love you")
2631728508784


011. 引用的本质 堆内存 和 栈 内存 

012. 标识符 帮助系统的简单使用 命名规则
	以双下划线开头和结尾的名称 通常有特殊含义， 尽量避免这种写法  __init__ 是类的构造函数

	帮助 F1
	
	
查看关键字：

help()

>>> sxt=123
>>> _sxt=234
>>> 3eds=3
SyntaxError: invalid syntax
>>> if=4
SyntaxError: invalid syntax
>>> help()

quit  退出 


013. 变量的声明 初始化 删除变量 垃圾回收

>>> a=123
>>> a
123
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a
NameError: name 'a' is not defined


014. 链式赋值   系列解包赋值 常量

链式赋值 用于 同一个对象赋值给多个变量 
x=y=123  相当于 x=123; y=123

系列解包赋值 
对应于相同个数的变量（个数必须保持一致）
a,b,c=4,5,6  a=4;b=5;c=6

a,b=1,2
a,b=b,a
print(a,b)


>>> a,b=1,2
>>> print(a,b)
1 2
>>> a,b=b,a
>>> print(a,b)
2 1
>>> 


python 不支持 常量 
MAX_SPEED=120 
print(MAX_SPEED)



015. 内置数据类型 基本算数运算符 
/ 浮点数除法 8/2=4.0
// 整数除法  7//2=3
%  取余   7%4=3
** 幂  2**3=8

>>> a=8/2
>>> a
4.0
>>> a=7/2
>>> a
3.5
>>> a=7//2
>>> a
3
>>> a=7%2
>>> a
1
>>> a=7%4
>>> a
3
>>> 2**3
8
'
>>> 2**10
1024
>>>


# 0 不能做 除数  
>>> 3/0
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    3/0
ZeroDivisionError: division by zero


divmod() 同时可以得到商和余数 
>>> divmod(10,3)
(3, 1)


016. 整数 不同进制 其他类型转换成整数 
使用 int() 实现类型转换
int(9.9)=9
int(True)=1
int("3434")=3434

int("34fecfv") error 

a=3+4.1
a
7.1 

>>> a=9.9
>>> id(a)
2196323636448
>>> b=int(a)
>>> id(b)
1947558304
>>> a
9.9
>>> id(a)
2196323636448


017. 浮点数

不改变原有值 生成新的对象  # important


四舍五入 round()

>>> a=3.14
>>> a
3.14
>>> float(3)
3.0
>>> b=3+4.6
>>> b
7.6
>>> int(3.76)
3
>>> round(3.54)
4
>>> round(4.67)
5
>>> 


>>> a=a+1
>>> a
4.140000000000001
>>> 

生成新的对象 4.14 把 4.14 的地址赋给 a 

增强运算符 a+=1 == a=a+1 



018. 时间表示 unix 时间点 毫秒 和 微秒 

>>> import time
>>> time.time()
1533788232.8670306
>>> b=int(time.time())
>>> b
1533788317
>>> totalMinutes=b/60
>>> totalMinutes
25563138.616666667
>>> totalMinutes=b//60
>>> totalMinutes
25563138
>>> totalHours=totalMinutes/60
>>> totalHours
426052.3
>>> totalDay=totalHours//24
>>> totalDay
17752.0


019. 多点坐标—— 绘出折线图 计算两点之间的距离 

import turtle 

x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100

turtle.goto(x1,y1)
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)



# start 
import turtle
import math

#定义多个点坐标
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100

#绘制折线
turtle.penup()
turtle.goto(x1,y1)

turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)


#计算起始点和终点的距离

distance=math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(distance)


20. 布尔值 比较运算符 逻辑运算符 
>>> a=10
>>> b=20
>>> a<b
True
>>> a!=b
True
>>> a==b
False
>>> a>b
False
>>> 


>>> a=True
>>> b=False
>>> a or b
True
>>> a or 30
True
>>> b or 30
30
>>> a or 30/0
True
>>> a and b
False
>>> a and 30
30
>>> b and a
False
>>> 


运算符    格式    说明 
or     x or y   x 为 true， 不计算 y , 直接返回 true  
                x 为false 则返回 y 

and    x and y  x 为 true 则返回y 的值
                x 为false 则不计算 y 直接返回 false  
not    not x       


021. 同一运算符 整数缓存的问题 

is   is 是判断两个标识符 是不是 引用 同一个对象 
is not    is not 是 判断 两个标识符是不是 引用不同对象 

 
is 是不是地址是一样的 

== 对象里的 value 值是不是一样的 

python 仅仅对 比较小的 整数对象进行缓存 [-5,256)
pycharm 的范围是[-5,任意数)

>>> a=1000
>>> b=1000
>>> a==b
True
>>> a is b
False
>>> id(a)
1490160995280
>>> id(b)
1490160994448
>>> c=10
>>> d=10
>>> c is d
True
>>> x=-6
>>> y=-6
>>> print(x is y)
False
>>> x=-5
>>> y=-5
>>> print(x is y)
True
>>> a=100000000000000000000000000001
>>> b=100000000000000000000000000001
>>> print(a is b)
False




022. 字符串  Unicode 字符集
三种创建字符串的方式 

>>> ord("A")
65
>>> ord('A')
65
>>> ord("师")
24072
>>> ord('师')
24072

>>> ord("Abel")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord("Abel")
TypeError: ord() expected a character, but string of length 4 found
>>> ord("a")
97



创建字符串： 用单引号 或者 双引号 

>>> a='sxt'
>>> a
'sxt'
>>> a="sxt"
>>> a
'sxt'



>>> a="sxt"
>>> a
'sxt'
>>> print(a)
sxt
>>> a='sxt-2'
>>> a
'sxt-2'
>>> print(a)
sxt-2
>>> a=" I' m a student"
>>> a
" I' m a student"
>>> b='my name si "Abel"'
>>> b
'my name si "Abel"'

多行字符串 
# 用连续的 ''' 或者 """ 
如：
>>> resume='''name="Abel"
company="sxt"
age=18 '''
>>> resume
'name="Abel"\ncompany="sxt"\nage=18 '
>>> print(resume)
name="Abel"
company="sxt"
age=18 
>>> 


>>> resume_1=""" name='Abel'
company='sxt'
age=18 """
>>> resume_1
" name='Abel'\ncompany='sxt'\nage=18 "
>>> print(resume_1)
 name='Abel'
company='sxt'
age=18



>>> resume='''name="Abel"
company="sxt"  age=19
lover="Tom"'''
>>> resume
'name="Abel"\ncompany="sxt"  age=19\nlover="Tom"'



python 允许 空字符串的存在 不包含任何字符且长度是0 

>>> c=""
>>> c
''
>>> len(c)
0
>>> len(a)
15
>>> len("sxt 哈哈哈哈")
8


023. 转义字符 字符串拼接 字符串复制 input() 获得键盘输入 

"\+特殊字符" 实现某些难以用字符串表示的效果 

>>> a='i\nlove\nyou'
>>> a
'i\nlove\nyou'
>>> print(a)
i
love
you
>>> b='i\'m a student'
>>> b
"i'm a student"
>>> print(b)
i'm a student

续行符
>>> print('aaa\
fhjeinfr')
aaafhjeinfr


字符串拼接 
'aa'+'bb'=='aabb'
（1）. 两边都是字符串 是字符串拼接 
（2）. 两边都是数字 加法运算 
（3）. 两边类型不同 抛出异常 

这样也可以 
>>> a='sxt'+'eric'
>>> a
'sxteric'  #新的对象 
>>> b='sxt''eric'
>>> b
'sxteric'


字符串的复制
>>> a='sxt'*3
>>> a
'sxtsxtsxt'
>>> 


不换行打印
# 这个必须使用 shell 写出来
print("aa",end="*")
print("bb",end="*")
print("cc")


从控制台上读取字符串
input()

>>> myname=input("please input your name: ")
please input your name: gapqi
>>> myname
'gapqi'
>>> print(myname)
gapqi
>>> 


024. 字符串 str()  提取字符串

>>> int(43.54)
43
>>> int("4343")
4343
>>> int("34.43")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("34.43")
ValueError: invalid literal for int() with base 10: '34.43'


str() 可以帮助将其他数据类型 转换成 字符串 
str(5.20)==>'5.20'
str(3.14e2) ==> '314.0' #科学计数法

>>> str("3432")
'3432'

>>> str(dksfndk)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    str(dksfndk)
NameError: name 'dksfndk' is not defined


str(True)==>'True' # 布尔值
>>> int("3434")
3434
>>> float("4.5556")
4.5556


使用 [] 提取字符
字符串 的本质是 字符序列 可以通过字符串后面添加 [].
在[] 里面指定偏移量 可以提取该位置的单个字符 

正向搜索： 直到 len(str)-1
反向搜索： 直到 -len(str)


正向所搜
>>> a="fhdjrencjefjrenfjnrejfrelahfijrelfxceuytiure"
>>> a[0]
'f'
>>> a[3]
'j'
>>> a[25]
'a'
>>> a[100]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[100]
IndexError: string index out of range

反向索搜
>>> a[-1]
'e'
>>> a[-2]
'r'
>>> 
>>> a[-25]
'e'
>>> a[-100]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[-100]
IndexError: string index out of range


replace 实现字符串的替换
实际上， 字符串对象不可变

>>> a="njdislnfuirewewoipreiutiureioscv"
>>> a[0]="A"
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[0]="A"
TypeError: 'str' object does not support item assignment
>>> a
'njdislnfuirewewoipreiutiureioscv'
>>> a.replace('i','高')
'njd高slnfu高rewewo高pre高ut高ure高oscv'
>>> a
'njdislnfuirewewoipreiutiureioscv'
#调用 replace 函数的时候 生成新的对象 新的字符串 
#原来的 a 没有发生变化


>>> b=a.replace('i','高')
>>> b
'njd高slnfu高rewewo高pre高ut高ure高oscv'
>>> 

也可以 
a=a.repalce() 



025. 字符串切片 slice 操作
截取子字符串 
[其实偏移量 start:, 终止偏移量end:, 步长step]

[:] 提取整个字符串  "abcdef"[:]   "abcdef"
[start:]  从start索引开始到结尾 "abcdef"[2:]  "cdef"
[:end]  从头开始到 end-1  "abcdef" [2:] "ab"
[start:end] 从 start 开始到 end-1  [2:4]  "abcdef"  "cd"
[start:end:step] 从 start 开始 到 end-1 步长是 step "abcdef"[1:5:2]  "bd"


>>> a="abcdefghijklmn"
>>> a[2]
'c'
>>> a[1:5]
'bcde'
>>> a[1:5:2]
'bd'
>>> a[1:5:3]
'be'
>>> a[1:5:1]
'bcde'
>>> a[:]
'abcdefghijklmn'
>>> a[2:]
'cdefghijklmn'
>>> a[:3]
'abc'
>>> 


三个量为负数 
a[-3:]   倒数三个 
a[-8:-3]  倒数第八个到倒数第三个
a[::-1]  步长为负数 从右到左 反向提取


>>> b="abcdefghijklmnopqrstuvwxyz"
>>> b[-3:]
'xyz'
>>> b[-8:-3]
'stuvw'
>>> b[::-1]
'zyxwvutsrqponmlkjihgfedcba'
>>> 

>>> b[2:30]
'cdefghijklmnopqrstuvwxyz'

超过范围 不会报错 

>>> "to be or not to be"[::-1]
'eb ot ton ro eb ot'
>>> "sxtsxtsxtsxtsxtsxt"[::3]
'ssssss'


026 字符串 切割 split() && join() 合并 
split() 可以基于指定分隔符将字符串 分割成 多个 子字符串 

用 split() && join()  得到是列表 
replace() 得到的还是 字符串 


>>> a="to be or not to be"
>>> a.split()
['to', 'be', 'or', 'not', 'to', 'be']
>>> a.split('be')
['to ', ' or not to ', '']
>>> a.split(' be ')
['to', 'or not to be']
>>> a.split(' be')
['to', ' or not to', '']


join() 用于将子字符串连接起来 
# join 一般和列表联系起来 
# 列表 用于储存多个对象

>>> b=['sxt','abel100','eric200']
>>> '*'.join(b)
'sxt*abel100*eric200'
>>> ' '.join(b)
'sxt abel100 eric200'

还有一种方法 
>>> 'sxt'+'abel100'+'eric200'
'sxtabel100eric200'

使用字符串凭借符 + 会产生新的字符串对象 不推荐使用
join() 函数 在拼接字符串之前会计算字符串的长度 逐一拷贝 仅新建一次对象 

#测试拼接符 和 join() 不同的效率

import time

time01=time.time()  #此时的时刻

a=""
for i in range(1000000):
    a+="sxt"

time02=time.time()  #finish

print("Total Time: "+str(time02-time01))


time03=time.time()  #start 
li=[]
for i in range(1000000):
    li.append("sxt")

a="".join(li)
time04=time.time()  #finish

print("Total Time: "+str(time04-time03))

OUT：
Total Time: 0.5230121612548828
Total Time: 0.1315011978149414

Total Time: 42.15147614479065
Total Time: 1.1187915802001953


027 字符串的驻留机制 和 字符串的比较 

字符串驻留： 仅保存一份相同且不可变字符串的方法， 不同的值被存档在字符串驻留池中。 

对于 符合标识符规则的会（_ 下划线 字母 数字 ）

>>> a="abd_33"
>>> b="abd_33"
>>> a is b
True
>>> id(a)
2093229631000
>>> id(b)
2093229631000

>>> c="dd#"
>>> d="dd#"
>>> c is d
False
>>> id(c)
2093229650808
>>> id(d)
2093229650976
>>> c==d
True


成员操作符
in not in 
判断某个字符（子字符串）是否在字符串中

>>> a="abcdefg"
>>> "b" in a
True
>>> "bcd" in a
True
>>> "ddd" in a
False
>>> "ddd" not in a
True



028. 字符串 常用方法 
常用的查找方法 

len(a)
a.startwith('')  True  False 
a.endwith('')   True False 
a.find('')   第一次出现指定字符串的位置 int
a.rfind('') 最后一次出现指定字符串位置  int 
a.count("")  指定的字符出现几次
a.isalnum() 所有的字符全是字母或者数字

>>> "fijewadej83er3".isalnum()
True


去除首位信息
strip() 去除字符串首尾指定信息 
lstrip()
rstrip() 

>>> "   sdjhjsda   ".strip()
'sdjhjsda'

>>> "  djsi djinwcjw dkmew  ".strip()
'djsi djinwcjw dkmew'

去除首尾空格 不是中间的 生成一个新的对象 

>>> "   sdjhjsda   ".strip()
'sdjhjsda'
>>> "  djsi djinwcjw dkmew  ".strip()
'djsi djinwcjw dkmew'
>>> "###shadijanbd#dshua##djiwlx###dkwlnjcx".strip("#")
'shadijanbd#dshua##djiwlx###dkwlnjcx'
>>> "***dmkewm**mclkdwmck***".strip("*")
'dmkewm**mclkdwmck'
>>> "***dmekwnmc**ckjdwnm**ckjw***".lstrip("*")
'dmekwnmc**ckjdwnm**ckjw***'
>>> "***dijewmni*dmekjwndjew*mkdwm***9887".rstrip("*")
'***dijewmni*dmekjwndjew*mkdwm***9887'
>>> "***fjif***".rstrip("*")
'***fjif'


大小写转化

a.capitalize(): 产生新的字符串， 首字母大写 
a.title()： 产生新的字符串，每个单词都首字母大写
a.upper()： 产生新的字符串，所有字符都转化成大写
a.lower()： 产生新的字符串，每个单词都首字母小写
a.swapcase()： 产生新的字符串， 所有字母大小写转化

>>> a="gaoqi loves programming, loves SXT"
>>> a.capitalize()
'Gaoqi loves programming, loves sxt'
>>> a.title()
'Gaoqi Loves Programming, Loves Sxt'
>>> a.upper()
'GAOQI LOVES PROGRAMMING, LOVES SXT'
>>> a.lower()
'gaoqi loves programming, loves sxt'
>>> a.swapcase()
'GAOQI LOVES PROGRAMMING, LOVES sxt'
>>> print(a)
gaoqi loves programming, loves SXT


格式排版
center() ljust()  rjust()
中间对齐  左对齐 右对齐

>>> a="sxt"
>>> a.center(10,"*")
'***sxt****'
>>> a.center(10)
'   sxt    '
>>> a.ljust(10,"*")
'sxt*******'
>>> a.rjust(10,"*")
'*******sxt'


其他方法
1. isalnum() 是否全为数字或者字母
2. isalpha() 检测字符串是否只有字母组成 （汉字）
3. isdigit() 检测字符串是否只有数字组成
4. isspace() 检测是否是空白符
5. isupper() 全是大写字母
6. islower() 全是小写字母 


029. 字符串的格式化 
format() 基本方法 
格式化字符串的函数 str.format() 增强了字符串格式化的功能 
基本语法是通过 {} 和 : 来代替以前的 %  
format 函数 可以接受不限个参数， 位置可以不按照顺序 

# 数字要按照 顺序 来填充 因为数字是索引位置


>>> a="name is: {0}, age is: {1}"
>>> a.format("Abel",18)
'name is: Abel, age is: 18'
>>> a.format("Eric",18)
'name is: Eric, age is: 18'
>>> b="name is: {0}, age is: {1}. {0} is a good boy"
>>> b.format("Eric",18)
'name is: Eric, age is: 18. Eric is a good boy'

>>> c="name is:{name},age is:{age}"
>>> c.format(age=18,name="Abel")
# 必须给出参数名 来传递



填充和对齐 

： 冒汗后面第一个是 填充的字符 
  ^    <     > 
居中 左对齐 右对齐 

>>> a="我是 {0}, 我喜欢数字{1:*^9}".format("Eric","666")
>>> a
'我是 Eric, 我喜欢数字***666***'

>>> a="我是 {0}, 我喜欢数字{1:*^9}".format("Eric","666")
>>> a
'我是 Eric, 我喜欢数字***666***'
>>> "我是 {0}, 我喜欢数字{1:^9}".format("Eric","666")
'我是 Eric, 我喜欢数字   666   '
>>> "我是 {0}, 我喜欢数字{1:#>9}".format("Eric","666")
'我是 Eric, 我喜欢数字######666'
>>> "我是 {0}, 我喜欢数字{1:*<9}".format("Eric","666")
'我是 Eric, 我喜欢数字666******'


数字的格式化 
浮点数通过 f 整数通过 d 进行需要的格式化

>>> a="我是 {0}, 我的存款有 {1:.2f}"
>>> a.format("Eric",437648.34)
'我是 Eric, 我的存款有 437648.34'

后面部分 不想看

030. 可变字符串
python中， 字符串属于不可变对象， 不支持原地修改
如果需要修改其中的值， 只能创建新的字符串对象 
如果要经常需要原地修改字符串， 可以使用 io.StringIO 对象 或者 array 模块

replace() # 生成新的对象

>>> s="hello, sxt"
>>> import io
>>> sio=io.StringIO(s)
>>> sio
<_io.StringIO object at 0x000002095E4B9318>
>>> sio.getvalue()
'hello, sxt'
>>> sio.seek(7)
7
>>> sio.write("g")
1
>>> sio.getvalue()
'hello, gxt'
>>> s
'hello, sxt'


031. 运算符总结 位操作符 
1. 比较运算符可以连用 并且含义相同
a=4
>>> 3<a<10
True

>>> a=0b11001
>>> b=0b01000
>>> c=a|b
>>> bin(c) #bin() 可以将数字转成二进制表示
'0b11001'
>>> c
25

>>> bin(a&b)
'0b1000'

>>> bin(a^b)
'0b10001'

2. 左移 右移 操作
运算速度快


3. 加法操作
数字相加
字符串拼接 
列表 元组等合并

>>> "3"+"2"
'32'
>>> "3"+2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    "3"+2
TypeError: must be str, not int

#元组 
>>> [10,20,30]+[5,10,100]
[10, 20, 30, 5, 10, 100]

4. 乘法操作
数字相乘 
字符串复制
列表 元组 复制

>>> 3*2
6
>>> "sxt"*3
'sxtsxtsxt'
>>> [10,20,30]*3
[10, 20, 30, 10, 20, 30, 10, 20, 30]

运算符的优先级
复杂表达式 用小括号组织 
1. 乘除优先加减
2. 位运算 和 算数运算 >  比较运算符 > 赋值运算符 > 逻辑运算符

(5+10*x)/5-13*(y-1)*(a+b)/x+9*(5/x+(12+x)/y)


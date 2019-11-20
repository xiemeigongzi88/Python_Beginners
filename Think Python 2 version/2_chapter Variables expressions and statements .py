2_chapter Variables expressions and statements 
page 27 


2.1 Assignment statements 赋值语句 
>>> message='and now for something completely different'
>>> message
'and now for something completely different'
>>> n=17
>>> n
17


#####################################
2.2 Variable names 变量名称

2.3 Expressions and statements 表达式和语句 
 
2.4 Script mode  脚本模式

2.5 Order of operations 运算符优先级 


#####################################
page 33 
2.6 String operations 字符串操作 

* + 可以使用 其余的不行 如
cant perform mathematical operations on strings, even 
if the strings look like numbers, so:
>>> '2'-'1'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    '2'-'1'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 'eggs'/'easy'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'eggs'/'easy'
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> '23'*'23'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    '23'*'23'
TypeError: can't multiply sequence by non-int of type 'str'

but there are two exceptions + *  

>>> first='throat'
>>> second='warbler'
>>> first+second
'throatwarbler'


>>> print('spam'*3)
spamspamspam

this use of + and * makes sense by analogy with addtion and multiplication 


###################################################
page 34 
2.7 Comments 

2.8 Debugging 

2.9 Glossary 术语列表 


###################################################
2.10 EXC_1
>>> x=y=1
>>> print(x)
1
>>> print(y)
1

EXC_2
(1) 
>>> math.pi
3.141592653589793
>>> pi=math.pi
>>> pi
3.141592653589793
>>> pi*(4/3)*5**3
523.5987755982989

(2)

























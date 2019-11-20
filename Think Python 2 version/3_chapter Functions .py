3_chapter Functions
page 40 

3.1 Function calls 
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'

>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159')
3.14159


page 41 
3.2 Math functions 

>>> import math
>>> math
<module 'math' (built-in)>



page 44 
3.4 adding new functions 

def print_lyrics():
    print("I am a lumberjack, and i am ok.")
    print("I sleep all night and I work all day")

print_lyrics()



page 46 
3.5 Definitions and uses 

def print_lyrics():
    print("I am a lumberjack, and i am ok.")
    print("I sleep all night and I work all day")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


page 47 
3.6 Flow of execution 


page 48 
3.7 Parameters and Arguments 形式参数和实际参数 

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')
print_twice(42)

print_twice("Spam"*4)

import math
print_twice(math.cos(math.pi))

OUT:
Spam
Spam
42
42
SpamSpamSpamSpam
SpamSpamSpamSpam
-1.0
-1.0


michael='Eric, the half a bee'
print_twice(michael)


3.8 Varibles and parameters are local 函数内部的变量和形式参数都是局部的 

def print_twice(bruce):
    print(bruce)
    print(bruce)

def cat_twice(part_1,part_2):
    cat=part_1+part_2
    print_twice(cat)

line_1='Bing tiddle'
line_2='tiddle bang'

cat_twice(line_1,line_2)

OUT：
Bing tiddletiddle bang
Bing tiddletiddle bang


page 51 
3.9 Stack diagrams 


page 53 
3.10 Fruitful functions and void functions 
 
def print_twice(bruce):
    print(bruce)
    print(bruce)

result=print_twice('Bing')
print(result)

Bing
Bing
None

the value None is not the same as the string 'None'.
it is a special value that has its own type

>>> print(type(None))
<class 'NoneType'>


page 54 
3.11 Why functions 


page 58 
3.14 EXC 

(1) 












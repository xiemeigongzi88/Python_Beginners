5_chapter Conditionals and recursion 
page 80 

5.1 Floor division and modulus 地板除和求模 

>>> minutes=105
>>> minutes/60
1.75
>>> minutes//60
1
>>> hour =minutes//60
>>> remainder=minutes-hour*60
>>> remainder
45


an alternative is to use the modulus operator % 
>>> remainder=minutes%60
>>> remainder
45


check whether one number is divisible by another 
-- if x%y is 0 then x is divisible by y 


page 81 
5.2 Boolean expressions 

>>> 5==5
True
>>> 5==6
False
>>> 5=6
SyntaxError: can't assign to literal


True and False are special values that belong to the type bool; they are not strings 

>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>

x!=y 
x>y
x<y
x>=y
x<=y


page 82 
5.3 Logical operators
there are three logical operators:
and or not 

the operands of the logical operators should be boolean expressions but python is not very strict 
any nonzero number is interpreted as True 

>>> 42 and True
True
>>> 0 and True
0
>>> 0 or True
True
>>> not 0
True

>>> 1 and 2
2
>>> 0 and 2
0

## so strange 


page 83 
5.4 Conditional execution 


PAGE 5.5 
5.5 alternative execution
if else 

5.6 Chained conditionals 链式条件 

if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x and y are equal')
    

page 85 
5.7 Nested conditionals 嵌套条件 

if x==y:
    print('x and y are equal')
    
else:
    if x<y:
        print('x is less than y')
    else:
        print('x is greater than y')


if x>0:
    if x<10:
        print('x is a positive single-digit number')
	
get same effect with the and operator 
	
		
if x>0 and x<10:
    print('x is a positive single-digit number')

	
page 87 
5.8 Recursion 

def countdown(n):
    if n<=0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
	
	
def print_n(s,n):
    if n<=0:
        return

    print(s)
    print_n(s,n-1)

s='python is good!'
n=4
print_n(s,n)


page 90 
5.10 infinite recursion 
def recurse():
    recurse()

recurse()


page 91 
5.11 Keyboard input 
text=input()
input: Eric 
'Eric'

name=input('what ... is your name?\n')

#name=input('what ... is your name?\n')


#text=input()

prompt="What ... is the airspeed velocity of an unladen swallow?\n"
speed=input(prompt) 
## input() 得到是字符串 ‘。。。’ 需要转化 

OUT:
What ... is the airspeed velocity of an unladen swallow?
42
>>> int(speed)
42
>>> speed
'42'



page 95 
5.14 EXC  



















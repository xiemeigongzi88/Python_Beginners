Think Python 2e 
Note

2_Chapter 

>>> first="throat"
>>> second="warbler"
>>> first+second
'throatwarbler'
 
 
>>> a="spam"
>>> a*3
'spamspamspam'
>>> a
'spam'


3_Chapter 

>>> import math
>>> math
<module 'math' (built-in)>


EXC 3_1
def right_justify(s):
    space=" "
    large_space=space*65
    a=large_space+s
    print(a)
    return a

b=right_justify('monty')
print(len(b))


OUT:
                                                                 monty
70


######################################
def print_spam():
    print('spam')

def do_twice(f):
    f()
    f()

do_twice(print_spam)

OUT:
spam
spam



5_Chapter 
EXC 5_1 

import math

def fermat(a,b,c,n):
    if(pow(a,n)+pow(b,n)==pow(c,n)):
        print("Holy smokes, Fermat was wrong!")
        return "work"
    else:
        return 'continue'

a=b=c=n=2

while(n>1):
    while(c>1):
        while(b>1):
            while(a>1):
                if(fermat(a,b,c,n)=="work"):
                    print(a,b,c,n)
                else:
                    a=a+1
            b+=1
        c+=1
    n+=1



6_Chapter

def absolute_value(x):
    if(x<0):
        return -x
    if x>0:
        return x


a=absolute_value(0)
print(a)

OUT:
None 

	
















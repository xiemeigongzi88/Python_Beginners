第十章 文件和异常 
page 91 - 102 

10.1 从文件中读取数据

要使用文本文件中的信息， 首先需要将信息读取到内存中， 
可以一次性读取文件的全部内容
也可以每次一行的方式 逐行读取 

10.1.1 读取整个文件 

pi_digits.txt  文件 
3.1415926535
8979323846
2643383279

file_reader.py 文件
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents)

OUT：
3.1415926535
8979323846
2643383279


要以任何方式使用文件—— 哪怕仅仅是打印内容， 也需要先打开文件 这样才能访问
函数 open() 接受一个参数， 就是要打开的文件的名称 

python 在当前执行的文件所在的目录中查找指定的文件  

当前运行的是 file_reader.py 文件， 因此 python 在 file_reader.py 所在的目录中 查找 pi_digits.txt 文件， 

函数 open() 返回一个表示文件的对象 
将这个对象存储在我们将在后面使用的变量中 

关键字 with 在不再需要访问文件后将其关闭 
这个程序中 调用了 open()  没有调用 close()
如果程序过早的 调用 close() ， 你会发现需要使用文件的时候， 它已经被关闭 了（无法访问） 
使用 with ， 只管打开文件 并在需要时使用它，python 会在合适的时候自动关闭文件 

使用 read() 方法 读取整个文件，文件的全部内容， 并将其作为一个长长的字符串存储子啊 常量 contents 中 


	相比于原始文件， 该输出唯一不同的地方时 末尾多了一个空行， 
	因为 read() 到达文件末尾时候返回一个空字符串 而将这个空字符串显示出来时 就是一个空行 
	
	要删除多出来的空行 可在 print中使用 rstrip()  
	
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())

	
	
10.1.2 文件路径
需要提供文件路径 它让python 到系统的特定位置查找 

在 Windows 系统中 在文件路径中使用 \ 
with open('text_files\filename.txt') as file_object:

绝对文件路径：
	绝对路径通常比相对路径 更长， 因此将其存储在一个变量中， 再将该变量传递给 open() 会有所帮助 

file_path='C:\Users\sxw17\Desktop\Python\files\Python Crash Course A Hands-On, Project-Based Introduction to Programming 1st Edition\10 Chapter'

file_path='C:\Users\sxw17\Desktop\Python\files\Python Crash Course A Hands-On, Project-Based Introduction to Programming 1st Edition\10 Chapter\pi_digits.txt'

with open(file_path) as file_object:


10.1.3 逐行读取 
要以每次一行的方式检查文件  可对文件对象使用 for 循环
 
filename="pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)

OUT:

3.1415926535

8979323846

2643383279

Note :
空白行： 在文件中， 每行的末尾都有一个看不见的换行符 可以使用 rstrip()去掉

filename="pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

OUT：
3.1415926535
8979323846
2643383279



10.1.4 创建一个包含文件各行内容的列表 
使用 关键字 with ， open() 返回的文件对象只在 with 代码块内使用 
如果 要在 with 代码块外访问文件的内容， 可在 with 代码块中 将文件的各行存储在一个列表中， 并在 with 代码块外使用该列表 ，
可以立即处理文件的各个部分， 也可以推迟到程序后面再 处理 


filename="pi_digits.txt"

with open(filename) as file_object:
    lines=file_object.readlines()
    
for line in lines:
    print(line.rstrip())

	
OUT：
3.1415926535
8979323846
2643383279

Note：
	readlines() 从文件中读取每一行， 并将其存储再一个列表中，
	该列表被存储到变量 lines 中， 
	
	with 代码块外， 依然可以使用这个变量 
	
>>> print(lines)
['3.1415926535\n', '8979323846\n', '2643383279\n']


readlines() 是 从文件中读取每一行， 并将其存储在一个列表中 


10.1.5 使用文件的内容 
	创建一个字符串， 包含文件中存储的所有数字 没有空格 
	
filename='pi_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string=pi_string+line.rstrip()

print(pi_string)
print(len(pi_string))


OUT：
3.141592653589793238462643383279
32


10.1.6 包含一百万位的大型文件

filename='pi_million_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''

for line in lines:
    pi_string+=line.strip()

print(pi_string[:52]+"...")
print(len(pi_string))


page 94
10.1.17 圆周率值中包含你的生日吗？

filename='pi_million_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''

for line in lines:
    pi_string+=line.rstrip()

birthday=input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("in the first million digits of pi!")
else:
    print("does not appear in the first million digits of pi.")



page 95
10.2 写入文件：
	保存数据的最简单的方式之一， 是将其写入文件中。
	
10.2.1 写入空文件 

filename='programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    

	
要将文本写入文件， 你在调用 open() 时 需要提供另一个实参 

调用 open() 时提供了两个实参， 第一个实参为要 打开的文件的名称，
第二个实参 ('w') 告诉 python 我们要以 写入模式 打开这个文件 

打开文件的时候：

读取模式 'r'
写入模式 'w'
附加模式 'a'
读取和 写入文件 'r+'

省略实参， 默认的是 只读模式 

如果写入的文件不存在， 函数 open() 将自动创建
以 ('w') 模式打开文件的时候要小心， 因为如果指定的文件已经存在， python 将在返回文件对象前 清空 该文件



10.2.2 写入多行 
函数 write() 不会再你写入的文本末尾添加换行符 
filename='programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
    
OUT：
I love programming.I love creating new games.


要让每个字符串都单独占一行， 需要再 write() 语句中包含换行符：

filename='programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    

OUT：
I love programming.
I love creating new games.



10.2.3 附加到文件 

如果要给文件添加内容， 而不是覆盖原有的内容，可以使用  附加模式 打开文件

以附加模式打开文件的时候， python 不会在返回文件对向前清空文件，而你写入到文件的行 都将添加 到文件末尾， 如果指定的文件不存在， python 会创建一个空文件 

filename='programming.txt'

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large detasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    
OUT：
I love programming.
I love creating new games.
I also love finding meaning in large detasets.
I love creating apps that can run in a browser.



page  96 
10.3 异常
	python 使用 异常 的特殊对象来 管理程序执行期间发生的错误 
	每当发生让 python 不知所措的错误的时候， 它都会创建一个异常对象，
	如果你编写了处理该异常的代码， 程序将继续 运行， 如果你未对异常进行处理， 程序将停止，并显示一个 traceback 其中包含有关异常的报告 
	
异常 是 使用 try-except 代码块处理的。
try-except 代码块让 python 执行指定的操作，同时告诉python 发生异常的时候， 怎么办 

使用了 try-except 代码块时候， 即便出现了异常， 程序也将继续运行；
显示你 编写的友好的错误信息， 而不是 trace back 


10.3.1 处理 ZeroDivisionError 异常 
>>> print(5/0)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(5/0)
ZeroDivisionError: division by zero

Note :
python 停止 运行程序， 并指出引发了哪种异常，而我们可以根据这些信息对程序进行修改，
下面告诉 python 遇到这种错误的时候 怎么办 

10.3.2 使用 try-except 代码块

try:
    print(5/0)
except ZeroDivisionError:
    print('You cannot divide by zero!')

    
OUT：
You cannot divide by zero!

Note：
如果 try 代码块中的代码运行起来没有问题， Python将跳过 except 代码块；
如果 try 代码块 中的代码导致了 错误， Python 将查找这样的 except 代码块， 并运行其中的代码块， 即其中指定的错误与引发的错误相同 


10.3.3 使用异常避免机制 

print("give me two numbers, and I ll divide them.")
print('Enter "q" to quit')

while True:
    first_number=input("\nFirst number: ")

    if first_number=='q':
        break;

    second_number=input('\nSecond number: ')

    if second_number=='q':
        break;

    answer=int(first_number)/int(second_number)

    print(answer)

OUT：
give me two numbers, and I ll divide them.
Enter "q" to quit

First number: 5

Second number: 0
Traceback (most recent call last):
  File "C:/Users/sxw17/PycharmProjects/9_class/test.py", line 15, in <module>
    answer=int(first_number)/int(second_number)
ZeroDivisionError: division by zero


10.3.4 else 代码块 
依赖于 try 代码块成功执行的代码都应该放到 else 代码块中：

print("give me two numbers, and I'll divide them.")
print('Enter "q" to quit')

while True:
    first_number=input("\nFirst number: ")

    if first_number=='q':
        break;

    second_number=input('\nSecond number: ')

    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you cannot divide it by zero!")
		
    else:  # important 
        print(answer)


Note:
	Python 尝试执行 try 代码块中的代码， 只有可能引发异常的代码才需要放在 try 语句中， 
	
	有一些仅在 try 代码块成功执行时才需要运行的代码，这些代码应该放在 else 代码块中 
	
	except 代码块告诉 python 如果它尝试运行 try 代码的时候引发了异常 该怎么办 
	

10.3.5 处理 FileNotFoundError 异常 

filename='alice.txt'

with open(filename) as f_obj:
    contents=f_obj.read()

OUT：
Traceback (most recent call last):
  File "C:/Users/sxw17/Desktop/Python/files/Python Crash Course A Hands-On, Project-Based Introduction to Programming 1st Edition/10 Chapter/alice.py", line 3, in <module>
    with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

##########################################

filename='alice.txt'

try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="sorry,the file "+filename+" does not exist."
    print(msg)

OUT：
sorry,the file alice.txt does not exist.


10.3.6 分析文本 

>>> title="Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']

方法 split() 以空格 为分隔符 将字符串拆成多个部分， 并将这些部分都存储在一个列表中。

结果时一个包含字符串中所有单词的列表，
虽然有些单词可能包含标点

filename='alice.txt'

try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="sorry,the file "+filename+" does not exist."
    print(msg)

else:
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")
    
OUT:
The file alice.txt has about 29461 words.


10.3.7 使用多个文件

def count_words(filename):

    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        msg="Sorry, the file "+filename + " does not exist."
        print(msg)
    else:
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words")

filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']

for filename in filenames:
    count_words(filename)

OUT:
The file alice.txt has about 29461 words
The file siddhartha.txt has about 42172 words
The file moby_dick.txt has about 215136 words
The file little_women.txt has about 189079 words


10.3.8 失败时一声不吭

def count_words(filename):

    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
       """ msg="Sorry, the file "+filename + " does not exist."
        print(msg)
		"""
		pass
		
    else:
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words")

filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']

for filename in filenames:
    count_words(filename)

Note :
Python 有一个 pass 语句， 可在代码块中使用它来让 python 什么都不要做 


10.3.9 决定报告哪些错误 




page 100 
10.4 存储数据
	用户关闭程序的时候， 几乎总是要保存提供的信息， 一种简单的方式就是使用 json 来存储数据 
	
模块 json 让你 能够将简单的 Python 数据结构转存到文件中，并在程序再次运行的时候 加载该文件的数据 

10.4.1 使用 json.dump()  && json.load()

编写一个存储数字的简短程序： json.dump() 
	再编写一个将这些数字读取到内存的程序  json.load() 
	
函数 json.dump() 接受两个实参： 要存储的数据  以及 可以用于存储数据的文件对象 

import json

numbers=[2,3,5,7,11,13]

filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

OUT：
[2, 3, 5, 7, 11, 13]

###################################3
import json

filename='numbers.json'
with open(filename) as f_obj:
    numbers=json.load(f_obj)

print(numbers)


OUT：
[2, 3, 5, 7, 11, 13]


10.4.2 保存和读取用户生成的数据

import json

username=input("what is your name?")

filename='username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("we will rememeber you when you come back, "+username+"!")

Eric

import json

filename='username.json'

with open(filename) as f_obj:
    username=json.load(f_obj)
    print("Welcome back, "+username+"!")


将这两个程序合并到一个程序中，尝试从文件中获取用户名， 

import json

filename='username.json'

try:
    with open(filename) as f_obj:
        username=json.load(f_obj)

except FileNotFoundError:
    username=input("what is your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("we ll remember you, when you come back, "+username+"!")
else:
    print("welcome back, "+username+"!")
        

		
		
10.4.3 重构
代码能够正确运行， 但可做进一步的改进， 将代码划分为 一系列完成具体工作的函数， 这叫做 重构 
import json

def greet_user():
    filename='username.json'

    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        username=input("Enter the name: ")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("remember you when you come back! "+username)
    else:
        print("Hi, "+username)


greet_user()



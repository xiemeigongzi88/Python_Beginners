6 面向对象和内存分析 
086-115  = 27 

086. 面向对象 和 面向过程 的区别 执行者思维


 
088. 类的定义  类和对象的关系 
类的结构：
	方法（函数） 行为 
	属性（变量） 状态
	
	
class Student:

    #属性需要定义在方法里
    def __init__(self,name,score):# self 必须有 必须位于第一个参数
        self.name=name
        self.score=score

    def say_score(self): #self必须位于第一个参数
        print("{0} 的分数是： {1}".format(self.name,self.score))


s1=Student("Erica",18)
s1.say_score()

OUT：
Erica 的分数是： 18
	

	
089. 构造函数 __init__
__init__() 方法：  给实例属性赋值 
__new__() 方法： 创建对象 一般无需重新定义该方法 


value 值：
	属性 (attribute)
	方法 （method）
	
	
名称固定： def __init__(slef,name,score):
第一个参数 必须是 self, 
定义的普通的方法 也必须是 self,

调用构造器：
	通过 类名（参数列表） 来调用 构造器 



090. 实例属性
实例属性 从属于 实例对象的属性 也称为 实例变量 要点：
1. 实例属性一般在  init 方法中定义
	self.实例属性名 = 初始值 

2. 本类的其他实例方法中， 也是通过 self 进行访问 
	self.实例属性名

3. 创建实例对象后， 通过实例对象访问
	obj01 =类名（）  #创建对象 调用 __init__() 初始化属性 
	obj01.实例属性名 =值  # 可以给已有属性赋值 也可以新加属性
	
	
class Student:

    #属性需要定义在方法里
    def __init__(self,name,score):# self 必须有 必须位于第一个参数
        self.name=name
        self.score=score

    def say_score(self): #self必须位于第一个参数
        print("{0} 的分数是： {1}".format(self.name,self.score))


s1=Student("Erica",18)
s1.say_score()
s1.age=18
s1.salary=40000

print(s1.salary)

del s1
print(s1.age)

s2=Student("Abel",98)
print(s2.name)
print(s2.age)


OUT：
Erica 的分数是： 18
Traceback (most recent call last):
40000
  File "C:/Users/sxw17/PycharmProjects/myPro_obj/mypy_01.py", line 20, in <module>
    print(s1.age)
NameError: name 's1' is not defined


091. 实例方法 
实例方法是 属于实例对象的方法 
格式：

def 方法名(self,[形参列表])
	函数体 
	
Note：
	定义方法 是不需要 self 的 
	但是 实例方法需要 self  这是区别 
	
方法的调用格式：
	对象.方法名（[形参列表]）
	
	
其他操作：
	1. dir(obj) 可以获得对象的所有属性 方法 
	2. obj._dict_  对象的属性字典
	3. pass  空语句
	4. isinstance(对象， 类型) 判断 “对象”  是不是 “指定类型”


class Student:

    #属性需要定义在方法里
    def __init__(self,name,score):# self 必须有 必须位于第一个参数
        self.name=name
        self.score=score

    def say_score(self): #self必须位于第一个参数
        print("{0} 的分数是： {1}".format(self.name,self.score))


s1=Student("Erica",18)
s1.say_score()
s1.age=18
s1.salary=40000

print(s1.salary)

print(s1.age)

s2=Student("Abel",98)
print(s2.name)


s2.say_score()

Student.say_score(s2) # 解释器调用的方法

print(dir(s2))

print(s2.__dict__)

class Man:
    pass

print(isinstance(s2,Student))
print(isinstance(s2,Man))

OUT：
Erica 的分数是： 18
40000
18
Abel
Abel 的分数是： 98
Abel 的分数是： 98
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'say_score', 'score']
{'name': 'Abel', 'score': 98}
True
False



092. 类对象

class Student:
    # 属性需要定义在方法里
    def __init__(self, name, score):  # self 必须有 必须位于构造器第一个参数
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于方法里第一个参数
        print("{0} 的分数是： {1}".format(self.name, self.score))


print(type(Student))
print(id(Student))

Stu2=Student

s1=Student("Eric",98)
s2=Stu2("Abel",100)

s1.say_score()
s2.say_score()


OUT：
<class 'type'>
1882792399464
Eric 的分数是： 98
Abel 的分数是： 100


093. 类属性 和 类方法 115-93=22
类属性 是从属于 “类对象” 的属性 也是 类变量 
类属性从属于类对象 可以 被所有实例对象共享 


类属性
class 类名:
		类变量名=初始值 
		
调用：
	类名.变量名
	
class Student:
    company="sxt"
    count=0

    def __init__(self,name,score):
        self.name=name
        self.score=score
        Student.count=Student.count+1

    def say_score(self):
        print("company is: ",Student.company)
        print(self.name," 's score is: ",self.score)

s1=Student("Erica",98)
s1.say_score()


s2=Student("Abel",94)
s3=Student("Ana",97)

print("create {0} Student object(s)".format(Student.count))

OUT:
company is:  sxt
Erica  's score is:  98
create 3 Student object(s)


094. 类方法 静态方法 
类方法通过 装饰器 @classmethod 来定义

@classmethod
	def  类方法名(cls [形参列表])
		函数体 
		
类方法中 访问实例属性 和 实例方法会 导致 错误 
子类继承父类方法的时候 传入cls 是子类对象 而非 父类对象 




#测试类方法

class Student:
        company="sct"

        @classmethod
        def printCompany(cls):
            print(cls.company)

Student.printCompany()

OUT：
sct


静态方法：
	静态方法需要 通过 “类调用”
	
	通过类名调用 不改变类里面参数的属性
		
	静态方法通过装饰器 @staticmethod 来定义 
	@staticmethod 
	def 静态方法名（[形参列表]）
		函数体 
		
	
调用静态方法格式：  类名.静态方法名（形参列表）
静态方法中访问实例属性和实例方法 会 导致错误 

#测试类方法 和 静态方法
class Student1:
    job="Programmer"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def printJob(cls):

        print(cls.job)
     #   print(self.name) #报错
        #类方法和 静态方法里 不能调用 实例变量 和 实例函数

Student1.printJob()


class Student:
    company="SXT"

    def __init__(self,name,age):
        self.name=name
        self.age=age


    @staticmethod
    def add(a,b):
        print("a+b=",a+b)
        print(Student.company)

      #  print(self.name)  # 报错
        return a+b

Student.add(2,3)

OUT：
Programmer
a+b= 5
SXT

类方法 和 静态方法中 访问 实例属性 和  实例方法 会导致错误 


095. __del__() 析构方法和垃圾回收 

__del__() 用于实现对象销毁时候 所需要的操作 
释放资源 


# 重写析构方法 
#析构方法

class Person:

    def __del__(self):
        print("销毁对象{0}".format(self))

p1=Person()
p2=Person()

del p2
print("over")



OUT：
销毁对象<__main__.Person object at 0x000001D719B0EAC8>
over
销毁对象<__main__.Person object at 0x000001D719B0EA90>


096. __call__() 方法 和 可调用对象
可调用对象 该对象可以像 函数一样被调用

返回字典
class SalaryAccount:
    '''工资计算'''

    def __call__(self, salary):
        print("beginning: ")
        yearSalary=salary*12
        daySalary=salary//27.5
        hourSalary=daySalary//8

        return dict(yearSalary=yearSalary,daySalary=daySalary,hourSalary=hourSalary)

s=SalaryAccount()
print(s(3000))

OUT：
beginning: 
{'yearSalary': 36000, 'daySalary': 109.0, 'hourSalary': 13.0}


097. 方法没有重载 方法的动态性
python 方法的参数 没有类型 
定义一个方法即可有多种调用方式 相当于重载 

#测试方法的动态性

class Person:

    def work(self):
        print("working...")

def play_game(s): #注意 这里有参数
    print("{0} is playing game.".format(s))

def work2(s):  #注意 这里有参数
    print("努力挣钱")


Person.play=play_game
p=Person()
p.work()
p.play()  # 实际传输的是： Person.play(p)

Person.work = work2
p.work()


OUT：

working...
<__main__.Person object at 0x00000143C470EB00> is playing game.
努力挣钱


098. 私有属性  实现封装
#测试私有属性

class Employee:

    def __init__(self,name,age):
        self.name=name
        self._age=age

e=Employee("Eric",18)

print(e.age)
print(e.name)

OUT：
AttributeError: 'Employee' object has no attribute 'age'


#######################################
#测试私有属性

class Employee:

    def __init__(self,name,age):
        self.name=name
        self.__age=age # 两个__ 

e=Employee("Eric",18)

#print(e.age)
print(e.name)


print(e._Employee__age) # 一个 _  两个 __
print(dir(e))



OUT：
Eric
18
['_Employee__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']


099. 私有方法 

# 测试私有属性

class Employee:
    __company = "Programmer"

    def __init__(self, name, age):  # 私有属性
        self.name = name
        self.__age = age

    def __work(self):  # 私有方法
        print("赚钱娶媳妇")
        print("age= {0}".format(self.__age))
        print(Employee.__company)


e = Employee("Eric", 18)

# print(e.age)
print(e.name)

print(e._Employee__age)
print(dir(e))

e._Employee__work()

print(Employee._Employee__company)


OUT：
Eric
18
['_Employee__age', '_Employee__company', '_Employee__work', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
赚钱娶媳妇
age= 18
Programmer
Programmer


100. @property 装饰器
可以将 一个方法的调用 变成 “属性调用 ”

#测试 @property 最简化的使用用法

class Employee:


    @property
    def salary(self):
        print("salary run...")
        return 10000

emp1=Employee()

print(emp1.salary)

emp1.salary=20000 #报错 不能赋值 只能调用 不能设置属性


OUT：
    emp1.salary=20000
AttributeError: can't set attribute



######################################
最土鳖版本
#@property 装饰器的用法

class Employee:

    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<10000:
            self.__salary=salary
        else:
            print("Error")

emp1=Employee("Eric",30000)
print(emp1.get_salary())
emp1.set_salary(2000)
print(emp1.get_salary())

OUT：
30000
2000


###############################
#@property 装饰器的用法

class Employee:

    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    @property
    def salary(self):
       return self.__salary

    @salary.setter
    def salary(self,salary):
        if 1000 < salary < 10000:
            self.__salary = salary
        else:
            print("Error")


emp1=Employee("Eric", 30000)
emp1.salary=-200

print(emp1.salary)


OUT：
Error 


101. 面向对象的三大特征
封装 
继承
多态



102. 继承
可以有 多个直接父类
#测试继承的基本使用

class Person:
    pass

class Student(Person):
    pass


print(Student.mro())

OUT:
[<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>]


################################################

父类里 私有的属性和私有的方法 
子类是继承了 但是不能直接用 

#测试继承的基本使用

class Person:

    def __init__(self,name,age):
        self.name=name
        self.__age=age


    def say_age(self):
        print("age I do not know")

class Student(Person):

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)  #必须显示的调用 不然不会被调用
        self.score=score


print(Student.mro())

s=Student("Erica",18,98)
s.say_age()

#print(s.age,)

print(dir(s))
print(s._Person__age)

OUT：
[<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>]
age I do not know
['_Person__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'say_age', 'score']
18



103. 方法的重写
类成员的继承 和 重写 
1. 成员继承： 子类继承了 父类 除了 构造方法之外的 所有成员 
2. 方法重写： 子类可以重写定义父类中的方法 这样就会覆盖父类的方法


#测试继承的基本使用 && 测试方法的重写

class Person:

    def __init__(self,name,age):
        self.name=name
        self.__age=age


    def say_age(self):
        print("age=",self.__age)

    def say_introduce(self):
        print("my name is； ",self.name)


class Student(Person):

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)  #必须显示的调用 不然不会被调用
        self.score=score

    def say_introduce(self): #覆盖父类方法 
        """重写父类的方法"""
        print("报告老师： my name is:",self.name)

s=Student("Eric",18,89)
s.say_age()
s.say_introduce()


OUT：
age= 18
报告老师： my name is: Eric




104.  object 根类

查看类的继承层次结构

通过 类的方法 mro() 或者 类的属性 __mro__ 可以输出这个类的继承层次结构

class A:pass
class B(A):pass
class C(B):pass

print(C.mro())


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_age(self):
        print(self.name, " 's age is: ",self.age)

obj=object()
print(dir(obj))

s2=Person("Eric",18)
print(dir(s2))

OUT:
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 

'age', 'name', 'say_age']


105. 重写 __str__() 方法
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def say_age(self):
        print(self.name, " 's age is: ",self.__age)

    def say_introduce(self):
        print("my name is:",self.name)

    def __str__(self):
        return "name is {0}".format(self.name)

p=Person("Eric",18)
print(p)  # object 默认的信息


OUT：
name is Eric

##########################################
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def say_age(self):
        print(self.name, " 's age is: ",self.__age)

    def say_introduce(self):
        print("my name is:",self.name)

p=Person("Eric",18)
print(p)  # object 默认的信息



OUT：
<__main__.Person object at 0x00000245BFE7EA58>



106. 多重继承 
支持多继承


107. mro() 函数 
如果多个父类有相同的名字的方法 
在子类没有指定 父类名时候， 解释器将从左到右 按顺序搜索

class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say AAA")

class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB")

class C(B,A):
    def cc(self):
        print("cc")

c=C()
c.cc()
c.bb()
c.say()
c.say()

print(C.mro())


OUT:
cc
bb
say BBB
say BBB
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]



108. super() 获得父类定义
class A:

    def say(self):
        print("A:",self)

class B:

    def say(self):
        A.say(self)
        print("B:",self)


B().say()

OUT：
A: <__main__.B object at 0x000001BD7383EAC8>
B: <__main__.B object at 0x000001BD7383EAC8>

###################################
class A:

    def say(self):
        print("A:",self)

class B(A):

    def say(self):
        #A.say(self)
        super().say()
        print("B:",self)


B().say()

OUT：
A: <__main__.B object at 0x000001E65BFFEAC8>
B: <__main__.B object at 0x000001E65BFFEAC8>



109. 多态
不同的实现
方法的多态  属性没有 多态 
必须要有  继承 和 方法重写 

#多态

class Man:
    def eat(self):
        print("饿了， 吃饭了")

class Chinese(Man):
    def eat(self):
        print("用筷子吃饭")

class English(Man):
    def eat(self):
        print("fork and knife")

class Indian(Man):
    def eat(self):
        print("hands")

def manEat(m):
    if isinstance(m,Man): # 对象 类 
        m.eat()
    else:
        print("cannot eat")

manEat(Chinese())

OUT：
用筷子吃饭


110. 特殊方法 和 运算符的重载 


















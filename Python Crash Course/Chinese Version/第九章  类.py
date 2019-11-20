 第九章  类
page 80 - 91 

9.1 创建和使用类：
9.1.1 创建 Dog 类 
class Dog():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")

       
	   
1. 方法 __init__() 
类中的 函数 = 方法 
		
方法 __init__() 形参 self 必不可少 还必须位于前面 


9.1.2 根据 类创建实例

class Dog():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")

my_Dog=Dog("whillie",6)

print("My dog's name is "+my_Dog.name.tilte()+".")
print("My dog is "+str(my_Dog.age)+" years old")


OUT：
My dog's name is Whillie.
My dog is 6 years old


1. 访问属性：
my_Dog.name

2. 调用方法：
class Dog():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")

my_Dog=Dog("whillie",6)
my_Dog.sit()
my_Dog.roll_over()


3. 创建多个实例
class Dog():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")

my_Dog=Dog("whillie",6)
your_Dog=Dog("lucy",3)

print("My dog's name is "+my_Dog.name.title()+".")
print("My dog is "+str(my_Dog.age)+" years old")
my_Dog.sit()

print("Your dog's name is "+your_Dog.name.title()+".")
print("Your dog is "+str(your_Dog.age)+" years old")

OUT：
My dog's name is Whillie.
My dog is 6 years old
Whillie is now sitting.
Your dog's name is Lucy.
Your dog is 3 years old


page 82 
9.2 使用类和实例
class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

OUT：
2016 Audi A4


9.2.2 给属性指定默认值

类中的每个属性都必须有初始值， 哪怕这个值是 0 或者 空字符串 
在方法 __init__() 内指定这种初始值是可行的；
如果对某个属性这样做， 就无需包含为它提供的初始值的形参 

class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

OUT：
2016 Audi A4
This car has 0 miles on it.


9.2.3 修改属性的值：
可以通过三种不同方式修改属性的值：
直接通过 实例进行修改， 通过方法进行设置 通过方法进行递增 

1. 直接修改属性的值：
class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23 #直接修改属性的值 
my_new_car.read_odometer()

OUT：
2016 Audi A4
This car has 23 miles on it.


2. 通过方法修改属性的值
class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def update_odometer(self,mileage):
        self.odometer_reading=mileage

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
print(my_new_car.odometer_reading)

OUT：2016 Audi A4
23



3. 通过方法对属性的值进行递增：
class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def update_odometer(self,mileage):
        self.odometer_reading=mileage

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)
print(my_new_car.odometer_reading)

my_new_car.increment_odometer(100)
print(my_new_car.odometer_reading)

OUT：
2016 Audi A4
23500
23600


page  84 
9.3 继承
	一个类 继承 另一个类的时候， 它将自动获得另一个类的所有属性和方法
	原来的类 称为父类， 新类 称为 子类 
	子类继承了其 父类的所有的属性和方法 同时还可以有定义自己的属性和方法 
	
9.3.1 子类的方法 __init__() 
	创建子类的实例的时候， Python首先需要完成的任务是 给父类的所有属性赋值 
	为此， 子类的方法 __init__()  需要父类施以援手
	
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class ElectricaCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year) #important 调用父类构造器

my_tesla=ElectricaCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())

OUT：

2016 tesla model s




9.3.3 给子类定义属性和方法
让一个类继承另一个类后， 可添加区分子类和父类的新属性和方法 

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class ElectricaCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=80

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

my_tesla=ElectricaCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

OUT：
2016 tesla model s
This car has a 80-kWh battery.


		
9.3.4 重写父类的方法：

	对于父类的方法， 只要它不符合子类模拟的实物的行为， 都可对其进行重写，
可在子类中定义一个这样的方法 ， 即 它与重要的父类方法同名， Python 将不会考虑这个父类方法， 而只关注你在子类中定义的相应的方法 


class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print("Fill the gas.")

class ElectricaCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=80

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def fill_gas_tank(self):
        print("This car does not need a gas tank.")


my_tesla=ElectricaCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

OUT：

2016 tesla model s
This car has a 80-kWh battery.
This car does not need a gas tank.
		
	

9.3.5 将实例用作属性：
		使用代码模拟实物的时候， 回发现自己给类添加的细节越来越多， 属性和方法清单 以及 文件都 越来越长 这种情况下， 可能需要将类的一部分作为一个独立的类提取出来， 可以将大型类拆分多个协同工作的小类 
		
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print("Fill the gas.")

class Battery():

    def __init__(self,battery_size=80):
        self.battery_size=battery_size

    def destribe_battery(self):
        print("This car has a "+str(self.battery_size)+" -kWh battery.")


class ElectricaCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
		#添加 battery 的属性 
		# 意思是 创建了一个 新的 Battery() 的实例变量
		# 并将实例变量存储在 self.battery这个变量中 

    def fill_gas_tank(self):
        print("This car does not need a gas tank.")


my_tesla=ElectricaCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.destribe_battery() ## important 
	
OUT：
2016 tesla model s
This car has a 80 -kWh battery.


###############################################
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print("Fill the gas.")

		
class Battery():

    def __init__(self,battery_size=80):
        self.battery_size=battery_size

    def destribe_battery(self):
        print("This car has a "+str(self.battery_size)+" -kWh battery.")

    def get_range(self):
        if self.battery_size==80:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go about: "+str(range)

        message+=" miles on a full charge"
        print(message)



class ElectricaCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def fill_gas_tank(self):
        print("This car does not need a gas tank.")


my_tesla=ElectricaCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())


my_tesla.battery.destribe_battery()
my_tesla.battery.get_range()


OUT： 
2016 tesla model s
This car has a 80 -kWh battery.
This car can go about: 240 miles on a full charge



page 87 
9.4 导入类
python允许将类存储在模块中 然后再主程序中导入所需的模块 

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print("Fill the gas.")

#导入类 
from car import Car

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23
my_new_car.read_odometer()



9.4.2 在 一个模块中存储多个类 
		
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print("Fill the gas.")

class Battery():

    def __init__(self,battery_size=80):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+" -kWh battery.")

    def get_range(self):
        if self.battery_size==80:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go about: "+str(range)

        message+=" miles on a full charge"
        print(message)

#虽然有两个类 但是只导入了 这个类 
class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
 

 
from car import ElectricCar

my_tesla=ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



## OUT：
2016 Tesla Model S
This car has a 80 -kWh battery.
This car can go about: 240 miles on a full charge


9.4.3 从一个模块中导入多个类 
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileadge):
        if mileadge>=self.odometer_reading:
            self.odometer_reading=mileadge
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print("Fill the gas.")

class Battery():

    def __init__(self,battery_size=80):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+" -kWh battery.")

    def get_range(self):
        if self.battery_size==80:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go about: "+str(range)

        message+=" miles on a full charge"
        print(message)


class ElectricCar(Car)：

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
  
  

from car import Car, ElectricCar # 注意 这里没有 ":" 

my_beetle=Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla=ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

OUT：
2016 Volkswagen Beetle
2016 Tesla Roadster




9.4.4 导入整个模块
代码导入的是 整个 car 模块

import car

my_beetle =car.Car("volkswagen",'beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla=car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())


OUT：
2016 Volkswagen Beetle
2016 Tesla Roadster


Note：
	注意导入的是 car.Car() 
	因为 import 只有 car 这个文件 
		
		
9.4.5 导入模块中的所有类：

from module_name import *

	这种导入方式没有明确指出你使用了模块中的哪些类
	
	需要从一个模块中导入很多类时候， 最好导入整个模块， 并使用 module_name.class_name 来访问类 
	虽然文件开头并没有列出用到的所有类， 但是你清楚知道了在程序的哪些地方使用了导入模块， 还能避免导入模块中的每个类可能引发的名称冲突 
	

9.4.6 在一个模块中导入另一个模块 

看不懂 



page  90 
9.5 Python 标准库
		
		
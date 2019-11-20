1. python 入门：
001-008

003 开发环境介绍 
cmd
enter: python 
>>> 提示符
ctrl+z or quit() // 退出python模式

死循环 退出
ctrl+c 程序中断 


004 IDLE 开发环境的使用 建立 Python源文件

IDLE ：
ctrl+n 


print("a")
print("b")
print("c")

Run --- Run module /F5

快捷方式 


005. Python程序格式—— 缩进——行注释 段注解 
行注释 ： # jdjdkn

段注释：
	'''
	sdjxn
	xskjnxd c 
	cdbhjw  
	'''
	
import turtle
t=turtle.Pen()

for x in range(360):
    t.forward(x)
    t.left(90)

	
	
006. 简单错误如何处理 守破离学习法 程序员修炼手册 

007. 海龟绘图 坐标系问题 画笔各种方法 

import turtle 
turtle.showturtle()
turtle.write("Eric")
turtle.forward(300)
turtle.color("blue")
turtle.left(90)
turtle.forward(300)
turtle.goto(0,50)
turtle.goto(0,0)
turtle.penup()
turtle.goto(0,300)
turtle.pendown()
turtle.circle(100)



008.海龟绘图 奥运五环图
#绘制奥运五环

import turtle

turtle.width(10)

turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)
turtle.pendown()

turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)
turtle.pendown()

turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)
turtle.pendown()

turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.pendown()

turtle.color("green")
turtle.circle(50)


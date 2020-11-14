#import the turtle
import turtle
t = turtle.Turtle()
s = turtle.Screen()
#how much money
total = 0
#ask's you how many pizzas
pizzas = input('how many pizzas')
total = total + int(pizzas)*10
#ask's you how many drinks
drinks = input('how many drinks')
total = total + int(drinks)*2
#greetings and money
print('welcome to suny side resteront')
print('that will cost $' ,total)
#what we accept
print('we accept 💳 or 💲')
#use the turtle
s.bgcolor('aqua')
t.color('gold')
t.penup()
t.forward(290)
t.left(90)
t.forward(150)
t.dot(130)
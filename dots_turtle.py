import turtle
from turtle import Turtle
import random
turtle.colormode(255)
tom=Turtle()
tom.speed("fastest")
tom.shape("circle")
for i in range(910):
    r=int(random.randint(0,255))
    g =int(random.randint(0,255))
    b =int(random.randint(0,255))
    tom.penup()
    tom.pencolor(r,g,b)
    tom.goto(random.randint(-300,300),random.randint(-300,300))
    tom.dot(10)
    tom.pendown()
tom.screen.mainloop()
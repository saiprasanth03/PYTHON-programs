import turtle
from turtle import Turtle
import random
turtle.colormode(255)
tom=Turtle()
tom.speed("fastest")
tom.shape("turtle")
tom.pensize(5)
for i in range(200):
    r=int(random.randint(0,255))
    g =int(random.randint(0,255))
    b =int(random.randint(0,255))
    tom.setheading(random.randrange(0, 360, 90))
    tom.pencolor(r,g,b)
    tom.forward(20)
tom.screen.mainloop()
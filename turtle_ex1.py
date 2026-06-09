import turtle
turtle.getscreen()

def triangle():
    turtle.forward(100)
    turtle.left(120)
def square():
    turtle.forward(100)
    turtle.left(90)
def pentagon():
    turtle.forward(100)
    turtle.left(72)
def hexagon():
    turtle.forward(100)
    turtle.left(60)
def heptagon():
    turtle.forward(100)
    turtle.left(51.42)
def octagon():
    turtle.forward(100)
    turtle.left(45)
def nine():
    turtle.forward(100)
    turtle.left(40)
def decagon():
    turtle.forward(100)
    turtle.left(36)

for i in range(3):
    triangle()
for i in range(4):
    square()
for i in range(5):
    pentagon()
for i in range(6):
    hexagon()
for i in range(7):
    heptagon()
for i in range(8):
    octagon()
for i in range(9):
    nine()
for i in range(10):
    decagon()
turtle.exitonclick()
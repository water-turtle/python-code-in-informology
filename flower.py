import turtle
import random
turtle.speed(speed=0)
for i in range(1000000) :
    x=random.randint(-420, 420)
    y=random.randint(-720, 720)
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()
    t=["red", "yellow", "blue", "green"]
    f=["red", "yellow", "blue", "green"]
    turtle.color(t[random.randint(0, 3)], f[random.randint(0, 3)])
    turtle.begin_fill()
    for j in range(5) :
        turtle.circle(30)
        turtle.left(72)
    turtle.end_fill()
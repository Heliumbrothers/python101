import random, sys, time
from turtle import Turtle, Screen
user = Turtle()
screen = Screen()
screen.screensize(1000, 1000)
step = 40
circle_radius = 40
colour_threshold = 255
screen.colormode(255)
layers = 1

user.penup()
user.goto((-485 - 135, -485))
user.pendown()
for i in range(0, int(screen.window_height()) // 15):
    for j in range(0, (screen.window_width() - 1) // (step * 2)):
        user.penup()
        user.forward(step * 2)
        user.pendown()
        user.color((random.randint(0, colour_threshold), random.randint(0, colour_threshold), random.randint(0, colour_threshold)))
        user.begin_fill()
        user.circle(circle_radius)
        user.end_fill()
    user.forward(step * 2)
    user.color((random.randint(0, colour_threshold), random.randint(0, colour_threshold), random.randint(0, colour_threshold)))
    user.begin_fill()
    user.circle(circle_radius)
    user.end_fill()
    user.forward(step)
    if layers % 2 == 1:
        user.left(90)
        user.penup()
        user.forward(4 * step)
        user.pendown()
        user.left(90)
        layers += 1
    else:
        user.right(90)
        user.penup()
        user.forward(step)
        user.pendown()
        user.right(90)
        layers += 1

screen.exitonclick()


from turtle import Turtle, Screen
colors = ['red', 'yellow', 'blue', 'green', 'black']
color = 0

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_left():
    tim.left(5)

def turn_right():
    tim.right(5)

def move_backward():
    tim.back(10)

def change_colour():
    global color
    tim.color(colors[color])
    if color == 4:
        color = 0
        tim.color(color)
    else:
        color += 1

def reset():
    tim.color('black')
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()



screen.listen()
screen.onkey(key='Up', fun=move_forward)
screen.onkey(key='Left', fun=turn_left)
screen.onkey(key='Right', fun=turn_right)
screen.onkey(key='Down', fun=move_backward)
screen.onkey(key='s', fun=change_colour)
screen.onkey(key='c', fun=reset)
screen.onkey(key='[', fun=pen_up)
screen.onkey(key=']', fun=pen_down)

screen.exitonclick()
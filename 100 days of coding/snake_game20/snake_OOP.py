from turtle import *
import time
screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
step = 20
DELAY = 0.01

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in range(0, len(STARTING_POS)):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(STARTING_POS[position])
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            screen.listen()
            screen.onkey(self.up, 'Up')
            screen.onkey(self.down, 'Down')
            screen.onkey(self.left, 'Left')
            screen.onkey(self.right, 'Right')
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            time.sleep(DELAY)
        self.segments[0].forward(step)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
    
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
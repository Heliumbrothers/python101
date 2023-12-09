from turtle import *
from snake_OOP import *
import random

class Food(Turtle, Snake):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.showturtle()
        self.color('Blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        #self.refresh()
    
    def refresh(self):
        self.goto(random.randint(-800, 800) / 2, random.randint(-800, 800) / 2)

    

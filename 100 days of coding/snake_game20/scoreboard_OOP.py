from turtle import *

screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('White')
        self.penup()
        self.goto((0, 500))
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', False, 'center', ('Courier New', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.write('GAME OVER', False, 'Center', ('Courier New', 24, 'normal'))


    
    
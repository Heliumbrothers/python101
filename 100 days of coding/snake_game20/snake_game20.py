from snake_OOP import *
from food_OOP import *
from scoreboard_OOP import *
import sys

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=1000, height=1000)
screen.title('Snake Game')
snake.create_snake()
game_is_on = True

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    windowheight = screen.window_height()
    windowwidth = screen.window_width()
    screen.update()
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.segments[0].xcor() > 1280 or snake.segments[0].xcor() < -1775 or snake.segments[0].ycor() > 725 or snake.segments[0].ycor() < -1410:
        game_is_on = False
        scoreboard.game_over()

time.sleep(1)
sys.exit()
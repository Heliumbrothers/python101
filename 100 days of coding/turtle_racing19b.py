from turtle import Turtle, Screen
import random, sys
screen = Screen()
screen_width = 1200
screen_height = 200
gap = 20
turtle_shape = 'turtle'
turtles = []
y_positions = [40, 20, 0, -20, -40]
colors = ['blue', 'green', 'black', 'gold', 'red']

screen.screensize(screen_width, screen_height)
user_bet = screen.textinput(title='Make Your Bet', prompt='Which turtle will win the race? Enter a colour (red, yellow, blue, green, black): ').lower()

for turtle_index in range(0, 5):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-600, y_positions[turtle_index])
    turtles.append(new_turtle)


while True:
    for turtle in turtles:
        if turtle.xcor() >= (screen_width / 2):
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\'ve won, The {winning_color} turtle is the winner!')
                sys.exit()
            else:
                print(f'You\'ve lost, The {winning_color} turtle is the winner!')
                sys.exit()
        distance = random.randint(0, 10)
        turtle.forward(distance)



from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY PYTHON SLITHER")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()
    
    if snake.segment[0].distance(food) < 15: # To check how close the snake is to the food
        food.new_location()
        snake.extend()
        scoreboard.increase_score() #increases score after every consumption

    # condition for when the snake comes in contact with any part of the walls
    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() > 290 or snake.segment[0].ycor() < -290:
        game_on = False
        scoreboard.game_over()

    # condition for when the snake head bits another part of the snake
    for seg in snake.segment:
        if seg == snake.segment[0]:
            pass
        elif snake.segment[0].distance(seg) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
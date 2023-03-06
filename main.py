from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

s = Snake()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    s.movement()


screen.exitonclick()
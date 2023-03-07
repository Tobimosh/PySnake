from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

s = Snake()
food = Food()

screen.listen()
screen.onkey(key="Right", fun=s.right)
screen.onkey(key="Left", fun=s.left)
screen.onkey(key="Up", fun=s.up)
screen.onkey(key="Down", fun=s.down)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    s.movement()


screen.exitonclick()
from turtle import Turtle
import random


class Food(Turtle):  # the class ''Food' is made to inherit properties of the Turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        xRand = random.randint(-280, 280)
        yRand = random.randint(-280, 280)
        self.goto(xRand, yRand)
        self.new_location()

    def new_location(self):
        xRand = random.randint(-280, 280)
        yRand = random.randint(-280, 280)
        self.goto(xRand, yRand)



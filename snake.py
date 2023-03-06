from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segment.append(snake)

    def movement(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

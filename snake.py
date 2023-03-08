from turtle import Turtle, Screen
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        self.create_snake()
        self.difficulty()

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_snake(position)
            
    def add_snake(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)
    
    def extend(self):
        self.add_snake(self.segment[-1].position())

    def movement(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def difficulty(self):
        level = self.screen.textinput(title="CHOOSE LEVEL", prompt="Choose a difficulty level (easy, medium, hard): ")
        if level == "easy":
            speed_multiplier = 0.5 
        elif level == "medium":
            speed_multiplier = 1 
        elif level == "hard":
            speed_multiplier = 2  
        else:
            print("Invalid difficulty level. Using easy.")
            speed_multiplier = 0.5
        
        # Set the speed of each segment based on the speed multiplier
        for seg in self.segment:
            seg.speed(int(10 * speed_multiplier))

        print("Segment speeds after changing difficulty level:")
        for segment in self.segment:
            print(segment.speed())



    def up(self):
        if self.segment[0].heading()!= DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)


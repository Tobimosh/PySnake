from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Times New Roman', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

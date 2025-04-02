from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.is_touched = False
        self.update_score()

    def update_score(self):
        self.clear()
        if (self.is_touched):
            self.score += 1
        self.goto(0, 225)
        self.write("scoreboard", align="center", font=("courier", 18, "bold", "italic"))
        self.goto(0,200)
        self.write(self.score, align="center", font=("courier", 18, "bold"))
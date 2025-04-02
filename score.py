from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lightgreen")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.is_touched = False
        self.update_score(0)

    def update_score(self, points):
        self.clear()
        if (self.is_touched):
            self.score += points
        self.goto(0, 220)
        self.write(f"score: {self.score}", align="center", font=("courier", 18, "bold", "italic"))
    
    def reset_score(self):
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Oops! Game Over", align='center', font=('courier', 20, 'bold'))
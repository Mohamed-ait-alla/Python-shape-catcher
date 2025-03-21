from turtle import Turtle

class Scope(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(350, -200)
        self.pendown()
        for i in range(1, 5):
            self.left(90)
            self.forward (700) if (i % 2 == 0) else self.forward (400)
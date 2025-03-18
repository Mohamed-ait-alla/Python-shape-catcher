from turtle import Turtle

class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        self.goto(0, -170)
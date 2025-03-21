from turtle import Turtle

class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        self.goto(0, -170)
    
    def move_bar_to_right(self):
        if (self.xcor() != 300):
            self.goto(self.xcor() + 20, self.ycor())
    
    def move_bar_to_left(self):
        if (self.xcor() != -300):
            self.goto(self.xcor() - 20, self.ycor())
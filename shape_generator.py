from turtle import Turtle
import turtle # for registering a shape
import random

class Shape(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_shapes()

    def generate_shapes(self):
        shapes_list = ["circle", "turtle", "square", "classic", "triangle", "arrow"]
        x_positions = list (range(-250, 250, 15))
        colors_list = ["red", "white", "yellow", "green", "blue", "cyan", "skyblue", "lightgreen", "light salmon", "purple"]
        self.shape(random.choice(shapes_list))
        self.color(random.choice(colors_list))
        self.penup()
        self.left(270)
        self.goto(random.choice(x_positions), 190)

    def go_down(self):
        if (self.ycor() < -200):
            self.hideturtle()
        self.goto(self.xcor(), self.ycor() - 5)
from turtle import Turtle
import turtle # for registering a shape
import random

class Shape(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_shapes()

    def generate_shapes(self):
        shapes_list = ["circle", "turtle", "square", "classic", "turtle", "triangle", "arrow", "turtle"]
        x_positions = list (range(-250, 250, 15))
        colors_list = ["red", "white", "yellow", "green", "white", "blue", "cyan", "white", "skyblue", "white", "lightgreen", "light salmon", "purple", "white"]
        self.shape(random.choice(shapes_list))
        self.color(random.choice(colors_list))
        self.penup()
        self.left(-90)
        self.goto(random.choice(x_positions), 190)

    def go_down(self):
        if (self.ycor() < -180):
            self.clear()
        self.goto(self.xcor(), self.ycor() - 5)
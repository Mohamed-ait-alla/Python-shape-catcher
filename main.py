from turtle import Screen, Turtle
from bar import Bar
from scope import Scope
from shape_generator import Shape
import time

# window setup
screen = Screen()
screen.title("shape catcher")
screen.setup(800, 500)
screen.bgcolor("black")
screen.tracer(0)

scope = Scope()
bar = Bar()
shapes = Shape()

# event handling
screen.listen()
screen.onkey(bar.move_bar_to_right, "Right")
screen.onkey(bar.move_bar_to_left, "Left")

while True:
    screen.update()
    time.sleep(0.1)
    shapes.go_down()
    if (shapes.ycor() < -190):
        shapes.generate_shapes()

screen.exitonclick()
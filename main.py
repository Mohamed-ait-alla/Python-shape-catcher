from turtle import Screen, Turtle
from bar import Bar
from scope import Scope
from shape_generator import Shape
from score import Scoreboard
import time

# window setup
screen = Screen()
screen.title("shape catcher")
screen.setup(800, 500)
screen.bgcolor("black")
screen.tracer(0)

scope = Scope()
bar = Bar()
shape = Shape()
score = Scoreboard()

# event handling
screen.listen()
screen.onkey(bar.move_bar_to_right, "Right")
screen.onkey(bar.move_bar_to_left, "Left")

while True:
    screen.update()
    time.sleep(0.1)
    shape.go_down()
    # when a shape goes arround generate another one
    if (shape.ycor() < -190):
        shape.generate_shapes()
    # check if a shape touch the bar
    if (bar.distance(shape) <= 40 and shape.ycor() <= -155):
        score.is_touched = True
        score.update_score()
        shape.clear()
        shape.generate_shapes()

screen.exitonclick()
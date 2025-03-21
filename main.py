from turtle import Screen, Turtle
from bar import Bar

# window setup
screen = Screen()
screen.title("shape catcher")
screen.setup(800, 500)
screen.bgcolor("black")
screen.tracer(0)

bar = Bar()

# event handling
screen.listen()
screen.onkey(bar.move_bar_to_right, "Right")
screen.onkey(bar.move_bar_to_left, "Left")

while True:
    screen.update()

screen.exitonclick()
from turtle import Screen, Turtle
from bar import Bar
from scope import Scope, Instructions
from shape_generator import Shape
from score import Scoreboard
import time

# window setup
screen = Screen()
screen.title("shape catcher")
screen.setup(800, 500)
screen.bgcolor("black")
screen.tracer(0)

# needed objects
scope = Scope()
instructions = Instructions()
bar = Bar()
shape = Shape()
score = Scoreboard()

# event handling
screen.listen()
screen.onkey(bar.move_bar_to_right, "Right")
screen.onkey(bar.move_bar_to_left, "Left")

def on_close():
    """ this function is responsible for exiting the window """
    screen.bye()

def start_game():
    """ this function is responsible for starting and ending the game"""
    game_on = True
    default_spead = 0.1
    points = 0
    instructions.clear()
    while game_on:
        screen.update()
        time.sleep(default_spead)
        shape.go_down()
        # when a shape goes arround generate another one
        if (shape.ycor() < -190):
            shape.generate_shapes()
        # when the shape touch the bar
        if (bar.distance(shape) <= 40 and shape.ycor() <= -155):
            score.is_touched = True
            shape_type = shape.shape()
            shape_color = shape.color()[0]
            # check break point and manage the points
            if (shape_type == 'turtle'):
                if (shape_color == 'white'):
                    game_on = False
                    score.game_over()
                    time.sleep(1)
                    screen.bye()
                    continue
                else:
                    points = 5
            elif (shape_type == 'circle' or shape_type == 'arrow'):
                points = 1
            elif (shape_type == 'square'):
                points = 2
            elif (shape_type == 'triangle' or shape_type == 'classic'):
                points = 0
                score.reset_score()
            # update the score and generate new shape
            score.update_score(points)
            shape.clear()
            shape.generate_shapes()
            default_spead *= 0.8

# start the game when ENTER key is pressed
screen.onkey(start_game, "Return")

# clean the window when the x button clicked
screen._root.protocol("WM_DELETE_WINDOW", on_close)
screen.exitonclick()
from turtle import Turtle

import setuptools

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.level = 1

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.setposition(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

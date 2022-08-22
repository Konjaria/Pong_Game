import turtle as t
from turtle import Turtle, tracer, update, goto
from random import randint


def x_axis(lower, upper):
    X_cor = randint(lower, upper)
    return X_cor


def y_axis(Lower, Upper):
    Y_cor = randint(Lower, Upper)
    return Y_cor


class bouncy(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_X = self.xcor() + self.xmove
        new_Y = self.ycor() + self.ymove
        self.goto(new_X, new_Y)

    def refresh(self):
        self.goto(0, 0)
        t.delay(1)
        self.goto(randint(-400, 400),randint(-300, 300))

    def y_modified(self):
        self.ymove *= -1
    
    def x_modified(self):
        self.xmove *= -1
        self.move_speed *= 0.1

    def reset_theposition(self):
        self.goto(0, 0)
        self.x_modified()
        self.move_speed = 0.1

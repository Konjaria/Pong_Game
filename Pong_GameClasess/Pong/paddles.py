from turtle import Turtle, update, tracer
import random

HEIGHT = 20
WIDTH = 100


class Paddles(Turtle):

    def __init__(self, X, Y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        tracer(0)
        self.goto(X, Y)
        update()

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def program_moves(self):
        random_list = [1, 2]
        final_act = random.choice(random_list)
        if final_act == 1:
            self.move_up()
        elif final_act == 2:
            self.move_down()

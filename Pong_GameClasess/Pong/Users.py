import turtle as t
from turtle import Turtle, tracer, update

FONT = ("Sylfaen", 24, "normal")


class User(Turtle):
    def __init__(self, Name, Game_Level, X, Y, ALIGNMENT="center"):
        super().__init__()
        self.done = Game_Level
        self.won = False
        self.score = 0
        self.alignment = ALIGNMENT
        self.name = Name  #
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(X, Y)
        self.write(f"{self.name}  :{self.score}", align=self.alignment, font=FONT)

    def update_scoreboard(self):
        self.write(f"{self.name}  :{self.score}", align=self.alignment, font=FONT)

    def increase_the_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def Winner_Revealed(self):
        if self.won:
            return f"{self.name} won the game"
        else:
            self.goto(200, 0)
            return f"{self.name} lost the game"

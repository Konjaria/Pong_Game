import turtle
from paddles import Paddles
import Ball
import time
from Users import User

screen = turtle.Screen()
screen.title("Pong game")
screen.setup(height=600, width=800)
screen.bgcolor("black")

acc1 = User("Saba", "easy", -350, 260, "left")
acc2 = User("Nikoloz", "easy", 350, 260, "right")
paddle_1 = Paddles(350, 0)
paddle_2 = Paddles(-350, 0)

screen.listen()
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_2.move_down, "s")
screen.onkey(paddle_2.move_up, "w")
PADDLES = [paddle_1, paddle_2]
game_is_on = True

ball = Ball.bouncy()
ball.speed("slow")
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Collision with a walls
    if abs(ball.ycor()) > 280:
        ball.y_modified()
    if ball.xcor() > 380:
        # game_is_on = False
        acc2.won = False
        acc1.increase_the_score()
        ball.reset_theposition()
    elif ball.xcor() < -380:
        # game_is_on = False
        acc1.won = False
        acc2.increase_the_score()
        ball.reset_theposition()
    # Collision with paddles
    if (ball.distance(paddle_1) < 40 and ball.xcor() > 340) or (ball.distance(paddle_2) < 40 and ball.xcor() < -340):
        ball.x_modified()


screen.exitonclick()

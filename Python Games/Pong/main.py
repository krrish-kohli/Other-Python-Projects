from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
# Setting up the screen.
screen.title("Pong: The Famous Arcade Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Creating the left and right paddle.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Creating the ball for the game.
ball = Ball()
# Creating the scoreboard.
scoreboard = Scoreboard()

screen.listen()
# Movements for the right paddle.
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
# Movements for the left paddle.
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Game loop.
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detects collision with the upper and lower walls and bounces off the ball.
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detects collision with the paddles and bounces off the ball.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -320):
        ball.bounce_x()

    # Detects if the paddles have missed the ball.
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

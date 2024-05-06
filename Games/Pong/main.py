""""
PONG GAME : 2 Player Game as Developed by ATARI
Components : Paddles, Ball, Net, Scoreboard.
"""
# TODO 1: Create Screen
# TODO 2: Create and move a paddle w=20,h=100,x=350,y=0
# TODO 3: Create and move another paddle
# TODO 4: Create and move ball
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle and bounce
# TODO 7: Detect miss by paddle
# TODO 8: Keep Score

from turtle import Screen

from Scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title('PONG 🏓')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)  # Turning off the animation, Need to manually update screen

paddle_left = Paddle((-350, 0))  # Goes +240 to -240.
paddle_right = Paddle((350, 0))

ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:
    # Feature Addition : Speed up ball !!
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()
    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    # Bug Fix : Resolves zigzag bug on paddle : Added check of direction (x_move)
    # Bug Fix : Resolves ball edge on paddle : Made distance 51 as by mathematics   
    if (ball.distance(paddle_right) < 51 and ball.xcor() > 320 and ball.x_move > 0) or (ball.distance(paddle_left) < 51 and ball.xcor() < -320 and ball.x_move < 0):
        ball.bounce_x()

    # Detect ball miss
    if ball.xcor() > 380:       # Detect Miss by Right Paddle
        ball.reset_position()
        score.lpoint()
    if ball.xcor() < -380:      # Detect Miss by Left Paddle
        ball.reset_position()
        score.rpoint()


screen.exitonclick()

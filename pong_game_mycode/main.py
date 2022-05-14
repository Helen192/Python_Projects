from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

l_paddle = Paddle(-380, 0)
r_paddle = Paddle(380, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# time_sleep is used to speed up the ball after the paddles hit the ball
time_sleep = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    ball.move()

    # detecting collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddles: ball move in another direction and the speed of ball is increased
    if (ball.distance(r_paddle) < 30 and ball.xcor() > 340 ) or (ball.distance(l_paddle) < 30 and ball.xcor() < -340):
        ball.bounce_x()
        time_sleep *= 0.6

    """if one paddle misses the ball, then:
    the ball comes back to the start position and then moves in another direction,
    score will be counted for the another paddle
    """
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.restart()
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.restart()

screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Show a box dialog where User enter the level (speed of the snake), at which they want to play the game.
    # User can choose one of these level: slowest, slow, normal, fast, fastest.
    # if the level user entered is not appropriate, then they have to choose again
flag = True
time_sleep = {"slowest": 0.3, "slow": 0.2, "normal": 0.1, "fast": 0.08, "fastest": 0.06} # each level has a different sleeping time of screen
while flag:
    level_user = screen.textinput("Choice of speed", "Please enter the speed (slowest/slow/normal/fast/fastest): ").lower()
    if level_user == "slowest" or level_user == "slow" or level_user == "normal" or level_user == "fast" or level_user == "fastest":
        flag = False

# screen.listen() and screen.tracer() have to line under the code of screen.texinput(). Otherwise all functions cannot function
    # this function is used to listen events on the screen
screen.listen()
    # this one will turn off the screen
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")

game_is_on = True
while game_is_on:
    # screen.update() is used to turn on the screen. We use this one because we have used screen.tracer(0) to turn off it
    screen.update()
    # after each time of updating the screen, it will take a break
    time.sleep(time_sleep[level_user])
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
        scoreboard.reset()
        scoreboard.game_over()
        game_is_on = False

    # Detecting collision with the tail.
        # if the head of snake hits any other part of the snake, then game is over
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()
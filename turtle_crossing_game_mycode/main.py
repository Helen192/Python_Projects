from turtle import Screen
from player import Player
from cars import Cars
from levelboard import LevelBoard
import time
import random
"""adding the function that user can choose the level of the game at the beginning.
    There are 3 level: easy, medium, difficult. For each level, the sleeping time of screen is different 
    Easy: time_sleep = 0.1
    Medium: time_sleep = 0.05
    Difficult: time_sleep = 0.02
"""
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# show a dialog where user can choose a game level
game_level = screen.textinput("GAME LEVEL", "Enter your level (easy/medium/difficult):").lower()
TIME_LEVEL = {"difficult": 0.02, "medium": 0.05, "easy": 0.1}
time_sleep = TIME_LEVEL[game_level]

# screen.listen() has to be below the screen.textinput. Otherwise player cannot move
screen.listen()

player = Player()
screen.onkey(player.go_up, "Up")

all_cars = Cars()
level_board = LevelBoard()

game_is_on = True

while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    all_cars.move()

    # create a new car every 6 seconds
    if random.randint(1, 6) == 3:
        all_cars.create_car()

    # When the player hits the top edge of the screen:
    # 1. it moves back to the original position and the player levels up
    # 2. On the next level, the car speed increases
    if player.ycor() > 280:
        player.staring_point()
        level_board.increase_level()
        time_sleep *= 0.7

    # When the player collides with a car, it is game over and everything stops
    for car in all_cars.car_list:
        if car.distance(player) < 15:
            level_board.game_over()
            game_is_on = False

screen.exitonclick()
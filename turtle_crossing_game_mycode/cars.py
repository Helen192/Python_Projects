from turtle import Turtle
import random

CAR_COLORS = ["pink", "yellow", "red", "blue", "green", "purple", "orange"]
MOVE_DISTANCE = 10


class Cars():

    def __init__(self):
        self.car_list = []
        self.create_car()

    def create_car(self):
        """create a new object car and add it to the car_list"""
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(CAR_COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-270, 270))
        new_car.setheading(180)
        self.car_list.append(new_car)

    def move(self):
        """every car in the car_list moves forward at a distance"""
        for car in self.car_list:
            car.forward(MOVE_DISTANCE)



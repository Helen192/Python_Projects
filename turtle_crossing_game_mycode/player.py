from turtle import Turtle
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.staring_point()

    def staring_point(self):
        """setting the start position of the player"""
        self.goto(0, -280)

    def go_up(self):
        """player will go up at a distance"""
        self.forward(MOVE_DISTANCE)

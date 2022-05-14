from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    # food will go to a random position on the screen
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


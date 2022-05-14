from turtle import Turtle

ALIGMENT = "left"
FONT = ("Courier", 24, "normal")


class LevelBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align=ALIGMENT, font=FONT)

    def increase_level(self):
        """increases level, clears the current level from the screen and then draws the increased level"""
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align= "center", font=FONT)

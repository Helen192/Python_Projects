from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open('Data.txt', mode='r') as data:
            self.highest_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    # update the current score
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    # increase the score whenever the snake hits the food
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # show the text "Game Over" on the screen
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=("Courier", 24, "normal"))

    # keep tracking the highest score
    def reset(self):
        # update the highest score
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('Data.txt', mode='w') as data:
                # convert self.highest_score to a string so that we can write the string to the Data.txt
                data.write(str(self.highest_score))

        # reset self.score to 0
        self.score = 0
        self.update_score()





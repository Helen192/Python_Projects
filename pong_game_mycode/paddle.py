from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.penup()
        self.goto(x_cor, y_cor)

    # move the l_paddle and r_paddle up and down
    def move_up(self):
        # if y_cor of the paddle is not bigger than 290, then it can continue to move up
        if self.ycor() < 290:
            self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        # if y_cor of the paddle is not smaller than - 290, then it can continue to move down
        if self.ycor() > -290:
            self.goto(self.xcor(), self.ycor() - 10)


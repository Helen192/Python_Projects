from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # ball move randomly to the above the wall
    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    # if the ball hits the top wall or bottom wall, then it bounces backward along y_cor
    def bounce_y(self):
        self.y_move *= -1

    # if the ball hits the paddles, it bounces backward along x_cor
    def bounce_x(self):
        self.x_move *= -1

    # restart the ball and move in another direction
    def restart(self):
        self.goto(0, 0)
        self.x_move *= -1

    def speed_up(self):
        self.x_move += 10
        #self.y_move += 10







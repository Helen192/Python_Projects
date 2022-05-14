from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake = []
        self.create_segment()
        self.head = self.snake[0]


    # create 3 squares with the same characters, and then append them to the snake (list)
    def create_segment(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    # create and add a new segment to the last position segment of the snake
    def extend(self):
        self.add_segment(self.snake[-1].position())

    # when the snake hits the wall or collides with their tail. Then:
    # 0. send the snake to the position outside of the screen
    # 1. The snake should be clear
    # 2. create a new snake
    #def reset(self):
    #    for seg in self.snake:
    #        seg.goto(1000, 1000)
    #    self.snake.clear()
    #    self.create_segment()
    #    self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].position())
        self.head.forward(MOVE_DISTANCE)


    # move the snake up, down, left or right. the way to move them is to move the first square of snake.
    # And then the second one will move to the position of the first, and the third one move to the position of the second square
    # make sure that if the snake is on the left, it cannot turn to the right and on right cannot turn to left
    # it the snake is up, it cannot move down. If it is down, it cannot move up
    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)









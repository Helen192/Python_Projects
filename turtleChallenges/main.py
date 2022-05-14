from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forwards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def curve():
    tim.circle(45, 45)

def clear_all():
    tim.clear()
    screen.resetscreen()


screen.listen()
screen.onkey(fun=forwards, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_all, key="c")
screen.onkeypress(fun=curve, key="Up")
screen.onkey(fun=curve, key="Down")
screen.exitonclick()

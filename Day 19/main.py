from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forwards():
    tim.forward(18)
def move_back():
    tim.back(18)
def turn_clcok_wise():
    tim.right(10)
def turn_counter_clock_wise():
    tim.left(10)
def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="d",fun=turn_clcok_wise)
screen.onkey(key="a",fun=turn_counter_clock_wise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
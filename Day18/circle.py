from turtle import Turtle,Screen,colormode
import random as rnd

tim=Turtle()
tim.shape("turtle")

tim.speed("fastest")
def change_color():
    R = rnd.random()
    B = rnd.random()
    G = rnd.random()
    tim.color(R, G, B)

for i in range (100):
    change_color()
    tim.circle(100)
    tim.setheading(tim.heading()+10)



















screen=Screen()
screen.exitonclick()
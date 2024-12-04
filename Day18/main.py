from turtle import Turtle,Screen,colormode
import random as rnd

tim=Turtle()
tim.shape("turtle")

def random_move(turtle_name):
    turtle_move=[turtle_name.backward,turtle_name.forward]
    turtle_direction=[turtle_name.right,turtle_name.left]

    rnd1=rnd.randint(0,1)
    rnd2=rnd.randint(0,1)

    turtle_direction[rnd2](90)
    turtle_move[rnd1](50)

def change_color():
    R = rnd.random()
    B = rnd.random()
    G = rnd.random()
    tim.color(R, G, B)

size=10
speed=0
tim.speed(0)
tim.pensize(size)
for i in range (3,50):
    random_move(tim)
    change_color()

















screen=Screen()
screen.exitonclick()
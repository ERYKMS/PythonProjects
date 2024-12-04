import random as rnd

from turtle import Turtle,Screen

tim = Turtle()
color_list = [ (234, 229, 232), (221, 231, 238), (145, 28, 66), (230, 237, 232), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35)]
list_len = len(color_list)


x=0
y=-180
tim.teleport(x, y)
for i in range(0,540):
    tim.dot(20,rnd.choice(color_list))
    tim.teleport(x, y)
    x+=60
    if x==600:
        x=0
        y+=60
print(tim.pos())


screen=Screen()
screen.exitonclick()

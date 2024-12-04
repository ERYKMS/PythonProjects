from turtle import Turtle,Screen
import random as rnd
is_race_on=False
screen=Screen()
screen.setup(500,400)
window_width=screen.window_width()
window_height=screen.window_height()
user_bet=screen.textinput(prompt="Whic turtle will win the race? Enter a color",title="Make Your Bet")

color_list=["yellow","green","blue","purple","brown"]

x=-230
y=-180
color_list_index=len(color_list)
all_turtles=[]
for i in range (0,color_list_index):
    new_turtle = Turtle(shape="turtle")
    new_turtle.teleport(x=x, y=y)
    new_turtle.color(color_list[i])
    y+=90
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            if turtle.pencolor()==user_bet:
                print(f"you win The {turtle.pencolor()} turtle is winner")

            else:
                print(f"you lose The {turtle.pencolor()} turtle is winner")

            is_race_on = False

        rand_distance=rnd.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()
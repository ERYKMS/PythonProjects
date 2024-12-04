from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen_wdth = screen.window_width()
screen_hght = screen.window_height()
screen.tracer(0)

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
scoreboard=Scoreboard()

reel_ball=Ball()


screen.listen()
screen.onkey(lambda :r_paddle.go_up(),"Up")
screen.onkey(lambda:r_paddle.go_down(),key="Down")

screen.onkey(lambda :l_paddle.go_up(),"W")
screen.onkey(lambda:l_paddle.go_down(),key="S")

game_is_on = True
while game_is_on:
    screen.update()
    reel_ball.move_ball()
    time.sleep(0.05)
    if reel_ball.ycor() >= 300 or reel_ball.ycor()<=-300:
        reel_ball.bounce()

    if reel_ball.distance(r_paddle)<50 and reel_ball.xcor()>340:
        reel_ball.paddle_bounce()
        reel_ball.speed_up()
        print(reel_ball.x_speed)

    if  reel_ball.distance(l_paddle)<50 and reel_ball.xcor()<-340:
        reel_ball.paddle_bounce()
        reel_ball.speed_up()
        print(reel_ball.x_speed)

    if reel_ball.xcor() >= 380:
        reel_ball.score()
        scoreboard.l_point()


    if  reel_ball.xcor() <= -380:
        reel_ball.score()
        scoreboard.r_point()


Screen().exitonclick()

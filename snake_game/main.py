from turtle import Screen
import time
import Snake
from scoreboard import  Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake.Snake()
food = Food()
score_board = Scoreboard()
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        score_board.reset()
        snake.reset()

    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    for segment in snake.segments[1::]:
        if snake.head.distance(segment)<10:
            score_board.reset()
            snake.reset()


screen.exitonclick()

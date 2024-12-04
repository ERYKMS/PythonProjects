from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.y_speed=+6
        self.x_speed=+6
        self.penup()


    def move_ball(self):
        self.speed(1)
        x_cor=self.xcor()
        y_cor=self.ycor()
        self.goto(x_cor +self.x_speed, y_cor + self.y_speed)

    def bounce(self):
        self.y_speed=self.y_speed*-1

    def paddle_bounce(self):
        self.x_speed=self.x_speed*-1

    def score(self):
        if self.xcor()>=380 or self.xcor()<=-300:
            self.teleport(0,0)

    def speed_up(self):
        if self.xcor()>0:
            self.x_speed-=0.05
            self.y_speed-=0.05
        else:
            self.x_speed+=0.05
            self.y_speed+=0.05













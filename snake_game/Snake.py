from turtle import Turtle

POSITION_LIST = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION_LIST:
            self.add_segmnet(position)
    def add_segmnet(self,position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
    def extend(self):
        self.add_segmnet(self.segments[-1].position())


    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(FORWARD_SPEED)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


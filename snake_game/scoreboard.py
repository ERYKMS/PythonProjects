from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score Board {self.score} High Score:{self.high_score}", align="center",font=("Arial",16,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("data", mode="w") as file:
                 file.write(str(self.score))
                 self.high_score=self.score
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        try:
            with open("data", mode="r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    #def game_over(self):
        #self.goto(0,0)
        #self.write("Game Over.",align="center",font=("Arial",16,"normal"))





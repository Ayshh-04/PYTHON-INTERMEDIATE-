

from turtle import Turtle

FONT = ("courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore=self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score},highscore:{self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open ("snake_dat.txt",mode="w") as file:
                file.write(str(self.highscore))
            self.score=0
            self.update_score()
    
    def read_highscore(self):
        with open ("snake_dat.txt",mode="r") as file:
                return int(file.read())

    # def game_over_statement(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.goto(0, -30)
        self.write(f"FINAL SCORE: {self.score}", align=ALIGNMENT, font=("courier", 15, "normal"))


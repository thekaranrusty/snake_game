from turtle import Turtle
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   move= False, align= "center", font= FONT)


    def score_refresh(self):
        self.score +=1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align="center", font=FONT)
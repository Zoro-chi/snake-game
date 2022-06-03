from turtle import Turtle

with open("data.txt") as data:
    high_score = int(data.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    Highscore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                updated_hs = str(self.high_score)
                data.write(updated_hs)
        self.score = 0
        self.update_scoreboard()





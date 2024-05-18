from turtle import Turtle

FONT = ("Courier", 14, "normal")
GAME_OVER_FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.score = 0
        self.write(arg=f"Level : {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game Over!", align="center", font=GAME_OVER_FONT)


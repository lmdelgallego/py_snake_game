from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard(self.score)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard(self.score)

    def update_scoreboard(self, score):
        self.clear()
        self.write(f"Score: {score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

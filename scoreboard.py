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
        self._writeScore(self.score)

    def update(self):
        self.score += 1
        self._writeScore(self.score)

    def _writeScore(self, score):
        self.clear()
        self.write(f"Score: {score}", align=ALIGNMENT,
                   font=FONT)

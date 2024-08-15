from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

    def display_score(self):
        self.clear()
        self.penup()
        self.goto(-280, 270)
        self.write(arg=f"Level: {self.level}", align="Left", font=FONT)
        self.hideturtle()

    def update_score(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="Center", font=FONT)

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        # Dimensions of the paddle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)

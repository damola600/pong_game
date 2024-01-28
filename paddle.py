# TODO: 2. Create and move a paddle
from turtle import Turtle

UP = 180
DOWN = 0
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        self.setheading(UP)
        x_cord = self.xcor()
        y_cord = self.ycor()
        self.goto(x_cord, y_cord + MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        x_cord = self.xcor()
        y_cord = self.ycor()
        self.goto(x_cord, y_cord - MOVE_DISTANCE)

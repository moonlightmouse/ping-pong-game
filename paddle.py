from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.setx(-380)
        self.sety(0)

    def move_up(self):
        self.forward(50)

    def move_down(self):
        self.backward(50)


from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1,1)
        self.penup()
        self.left(30)
        self.goto(0,0)
        self.speed('slowest')

    def turnleft(self):
        self.setheading(180)
        self.left(30)

    def turnright(self):
        self.setheading(0)
        self.right(30)

    def turnup(self):
        self.setheading(90)
        self.right(45)

    def turndown(self):
        self.setheading(270)
        self.left(45)
from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.setheading(270)
        self.pencolor('white')

        while self.ycor() > -300:
            self.forward(20)
            if self.ycor() % 40 == 0:
                self.penup()
                continue
            self.pendown()

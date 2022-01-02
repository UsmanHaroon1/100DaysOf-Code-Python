from turtle import Turtle
from turtle import Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.cs=0
        self.setposition(0,280)
        self.shapesize(3,3)
        self.display()

    def display(self):
        self.write(f"Score is {self.cs}",move=False,align="center",font=('Arial', 15, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write(f"GameOver", False, align="center",font=('Arial', 30, 'normal'))

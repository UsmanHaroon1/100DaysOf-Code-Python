from turtle import Turtle
from turtle import Screen

class Pongbat(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4,stretch_len=0.5)
        self.penup()
        self.goto(position)

    def up(self):
        self.sety(self.ycor()+40)
        Screen().update()

    def down(self):
        self.sety(self.ycor() - 40)
        Screen().update()


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
        with open("highscore.txt",'r') as f:
            self.hs=int(f.read())
        self.setposition(0,270)
        self.shapesize(3,3)
        self.display()

    def display(self):
        self.write(f"Score:{self.cs}",move=False,align="right",font=('Arial', 15, 'normal'))
        self.write(f"HighScore:{self.hs}",move=False,align="left",font=('Arial', 15, 'normal'))
    def gameover(self):
        self.goto(0,0)
        self.write(f"GameOver", False, align="center",font=('Arial', 30, 'normal'))

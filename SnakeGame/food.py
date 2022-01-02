from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5,0.5)
        self.refreshposition()

    def refreshposition(self):
        self.goto(random.randint(-300,300),random.randint(-300,300))

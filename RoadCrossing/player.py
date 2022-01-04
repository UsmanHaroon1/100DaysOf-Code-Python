from turtle import Turtle
import random

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('brown')
        self.penup()
        self.goto(0,-240)
        self.setheading(90)

    def moveup(self):
        self.forward(50)
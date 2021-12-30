from turtle import Turtle
import random

class Food:

    def __init__(self):
        food = Turtle('circle')
        food.color('blue')
        food.penup()
        food.goto(random.randint(-300,300),random.randint(-300,300))
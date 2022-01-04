from turtle import Turtle
import random
COLORS = ['red','blue','black','violet','purple','cyan']
class Car:
    def __init__(self):
        self.listcars = []

    def createcar(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(240,random.randint(-200,200))
            new_car.setheading(180)
            self.listcars.append(new_car)


    def move(self):
        for car in self.listcars:
            car.forward(10)
from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import Car
from scorecard import Score
import time

screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor('white')
screen.title('Road crossing game')

screen.tracer(0)
turtle = Player()
car = Car()
score = Score()
is_game_on = True

screen.update()
screen.listen()
screen.onkey(turtle.moveup,"Up")

while is_game_on:
    #To speedup cars at each level
    time.sleep(0.1 / score.level)
    screen.update()

    car.createcar()
    car.move()
    if turtle.ycor()>220:
        score.incrementscore()
        score.updatescore()
        for cars in car.listcars:
            cars.goto(1000,1000)
        #moving turtle to initial location after each level
        turtle.goto(0,-240)

    #Collision with car
    for onecar in car.listcars:
        if turtle.distance(onecar) < 25:
            is_game_on = False
            score.gameover()

screen.exitonclick()
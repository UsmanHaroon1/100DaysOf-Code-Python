from turtle import Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600,height=600)
screen.title('Welcome to Snake game')
screen.bgcolor('black')
colors = ('red','green','orange')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.moveforward()

screen.exitonclick()

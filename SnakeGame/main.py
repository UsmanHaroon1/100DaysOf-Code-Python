from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(width=600,height=600)
screen.title('Welcome to Snake game')
screen.bgcolor('black')
colors = ('red','green','purple')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.moveforward()

    #Collision with food
    if snake.head.distance(food)<15:
        food.refreshposition()
        snake.addSegment()
        score.cs+=1
        score.clear()
        score.display()
        screen.update()

    # Collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 15:
            is_game_on = False

    # Collision with wall
    if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
        is_game_on = False

score.gameover()

if score.cs > score.hs:
    with open("highscore.txt",'w') as f:
        f.write(str(score.cs))
screen.exitonclick()

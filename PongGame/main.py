import time
from turtle import Screen
from separator import CenterLine
from paddle import Pongbat
from ball import Ball
gamescreen = Screen()
gamescreen.setup(width=600,height=600)
gamescreen.bgcolor('black')
gamescreen.title('Welcome to PingPong')
gamescreen.tracer(0)

cl = CenterLine()
leftbat = Pongbat((-300,0))
rightbat = Pongbat((293,0))

gamescreen.listen()
gamescreen.onkey(leftbat.up,'w')
gamescreen.onkey(leftbat.down,'s')

gamescreen.onkey(rightbat.up,'Up')
gamescreen.onkey(rightbat.down,'Down')

#Creating ball
gamescreen.tracer(1)
ball = Ball()
ball.speed("slowest")

print(leftbat.xcor())
print(rightbat.xcor())
while ball.xcor() < 295 and ball.xcor() > -302:
    time.sleep(0.01)
    ball.forward(2)

    #Collided with paddle
    if rightbat.distance(ball) < 30 and ball.xcor() < 280:
        print('collided with right bat')
        ball.turnleft()

    if leftbat.distance(ball) < 30 and ball.xcor() > -280:
        print('collided with left bat')
        ball.turnright()

    #Collided with wall
    if ball.ycor() < -270:
        print('collided with down wall')
        ball.turnup()

    if ball.ycor() > 290:
        print('collided with up wall')
        ball.turndown()

print(ball.xcor())
print(ball.ycor())
print('Over')
gamescreen.update()
gamescreen.exitonclick()

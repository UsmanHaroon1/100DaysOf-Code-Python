import colorgram
import turtle as t
import random

t.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(tuple(color.rgb))

tiny = t.Turtle()
tiny.penup()
tiny.hideturtle()
tiny.setheading(225)
tiny.forward(400)
tiny.setheading(0)
tiny.speed('fastest')
for i in range(1,101):
    tiny.dot(20,random.choice(rgb_colors))
    tiny.forward(50)

    if i%10 == 0:
        tiny.setheading(90)
        tiny.forward(40)
        tiny.setheading(180)
        tiny.forward(500)
        tiny.setheading(0)

t.Screen().exitonclick()

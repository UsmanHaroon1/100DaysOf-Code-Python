from turtle import Turtle,Screen
import pandas

screen = Screen()
bg = "blank_states_img.gif"
screen.bgpic(bg)
turtle = Turtle()
turtle.hideturtle()
turtle.penup()

data = pandas.read_csv('50_states.csv')

answer = ""
while answer != 'Exit':
    answer = screen.textinput("Guess the state", "Enter the state name").title()
    screen.onscreenclick
    if answer == 'Exit':
        break
    states = data.state.to_list()
    if answer in states:
        coord = data.loc[data['state'] == answer]
        turtle.goto(int(coord.x),int(coord.y))
        turtle.write(f'{answer}')

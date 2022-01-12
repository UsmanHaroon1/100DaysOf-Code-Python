from turtle import Turtle,Screen
import pandas

screen = Screen()
bg = "blank_states_img.gif"
screen.bgpic(bg)
turtle = Turtle()
turtle.hideturtle()
turtle.penup()

data = pandas.read_csv('50_states.csv')
answer=""
found_states = []
while answer != 'Exit':
    answer = screen.textinput("Guess the state", "Enter the state name").title()
    if answer == 'Exit':
        break
    states = data.state.to_list()
    if answer in states:
        found_states.append(answer)
        coord = data.loc[data['state'] == answer]
        turtle.goto(int(coord.x),int(coord.y))
        turtle.write(f'{answer}')

missed_states = [state for state in states if state not in found_states]

missed_states_df = pandas.DataFrame(missed_states,columns=["Missed states"])
missed_states_df.to_csv('states_to_learn.csv')

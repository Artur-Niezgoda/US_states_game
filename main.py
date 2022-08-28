import turtle
import pandas as pd
from state_name import StateName

# path for the image
IMAGE_PATH = "blank_states_img.gif"

# Creating Screen object
state_name = StateName()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Read data
data = pd.read_csv("50_states.csv")
guessed_states = []
guessed_capitols = []

# Part of the game where user gives names of the states
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"({len(guessed_states)}/50) states correct.",
                              prompt="What's another state's name?").title()
    if answer in ["Quit", "Q", "Exit"]:
        break
    if answer in data["state"].unique() and answer not in guessed_states:
        row = data.loc[data.state == answer]
        state_name.add_name(row.state.item(), row.x.item(), row.y.item())
        guessed_states.append(row.state.item())

# Part of the game where user tries to give names of the capitols of the previously provided correct names of the states
for i in range(len(guessed_states)):
    name = guessed_states[i]
    row = data.loc[data.state == name]

    answer = screen.textinput(title=f"({len(guessed_capitols)}/{len(guessed_states)}) state's capitols correct.",
                              prompt=f"What's capitol of {row.state.item()}?").title()
    if answer in ["Quit", "Q", "Exit"]:
        break
    if answer == row.capitol.item():
        state_name.states_list[i].clear()
        state_name.add_name(row.state.item(), row.x.item(), row.y.item(), color="green")
        guessed_capitols.append(answer)
    else:
        state_name.states_list[i].clear()
        state_name.add_name(row.state.item(), row.x.item(), row.y.item(), color="red")

# Create DataFrame of the list of the missed states and capitols
states_to_learn = data[~data.state.isin(guessed_states)].state
capitols_to_learn = data[~data.capitol.isin(guessed_capitols)][['state', 'capitol']]

# Save DataFrames to csv files
states_to_learn.to_csv("states_still_to_learn.csv")
capitols_to_learn.to_csv("capitols_still_to_learn.csv")

screen.exitonclick()

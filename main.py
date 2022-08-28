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
guessed = []

while len(guessed) < 50:
    answer = screen.textinput(title=f"({len(guessed)}/50) states correct.",
                              prompt="What's another state's name?").title()
    if answer in ["Quit", "Q", "Exit"]:
        break
    if answer in data["state"].unique():
        row = data.loc[data.state == answer]
        state_name.add_name(row.state.item(), row["x"].values[0], row["y"].values[0])
        guessed.append(row.state.item())

states_to_learn = data[~data.state.isin(guessed)].state
states_to_learn.to_csv("states_still_to_learn.csv")

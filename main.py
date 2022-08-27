import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE_PATH = "blank_states_img.gif"
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)


answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer)
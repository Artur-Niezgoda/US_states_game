from turtle import Turtle

class StateName:

    def __init__(self):
        self.states_list = []

    def add_name(self, name, x, y):
        new_name = Turtle()
        new_name.penup()
        new_name.hideturtle()
        new_name.goto((x, y))
        new_name.write(name.capitalize())
        self.states_list.append(new_name)

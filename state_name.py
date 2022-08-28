"""
Module for U.S. state quiz game. Creates turtle objects on proper position everytime users gives
correct name of the state.

Classes:
    StateName

Methods:
    add_name(name, x, y)
        add name of the state to the map according to the coordinates x, y
"""

from turtle import Turtle


class StateName:
    """
    Create an object that displays text on the map in the correct place.

    Attributes:
        states_list: a list holding all the objects
    """

    def __init__(self):
        self.states_list = []

    def add_name(self, name: str, x: float, y: float, color: str = "black") -> None:
        """
        Create a turtle object at position given by x, y by printing name in the given color and add it to the list
        :param name: correctly spelled name of the state
        :param x: x coordinate
        :param y: y coordinate
        :param color: color of the text (default black)
        """

        new_name = Turtle()
        new_name.color(color)
        new_name.penup()
        new_name.hideturtle()
        new_name.goto((x, y))
        new_name.write(name.title())
        self.states_list.append(new_name)

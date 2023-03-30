# U.S. States Quiz Game

This is a Python-based quiz game that tests the user's knowledge of U.S. states and their capitols. The game displays a blank map of the U.S. with the names of states missing. The user is then prompted to input the names of the states they know, and the program will display the name of the state in the correct location on the map.

Once the user has entered all 50 states, they will then be prompted to enter the name of the capitol city for each state they previously named correctly. If the user enters the correct name, the state name on the map will turn green. If they enter the incorrect name, the state name will turn red. 

After the game is completed, the program will generate two CSV files, one containing the names of the states that the user failed to correctly guess, and one containing the names of the state capitols that the user failed to guess correctly.

## Usage

To play the game, simply run the `main.py` file. The game will open in a new window and prompt the user to enter the names of the states they know. Once the user has entered all 50 states, they will then be prompted to enter the name of the capitol city for each state they previously named correctly.

## Files

- `main.py`: the main file that runs the game
- `50_states.csv`: a CSV file containing the names of all 50 U.S. states and their corresponding x and y coordinates on the map
- `state_name.py`: a Python module that creates turtle objects on the map in the correct location every time a user inputs a correctly spelled state name
- `blank_states_img.gif`: a GIF file that displays a blank map of the U.S.
- `states_still_to_learn.csv`: a CSV file that contains the names of the states that the user failed to guess correctly
- `capitols_still_to_learn.csv`: a CSV file that contains the names of the state capitols that the user failed to guess correctly

## Dependencies

- Python 3
- pandas
- turtle

# U.S. States Game

This is a Python project that allows you to play a simple guessing game to learn the U.S. states using the `turtle` and `pandas` libraries. In this game, you will be presented with a blank map of the U.S. states, and you need to guess the names of the states.

## Prerequisites
Before running the game, you'll need to make sure you have the following installed:

- Python: This project was written in Python, so you'll need a working Python installation.
- `turtle` library: This library is used for creating graphics and drawing on the screen.
- `pandas` library: This library is used for reading data from a CSV file.

## How to Play
1. Clone this repository to your local machine or download the source code.

2. Make sure you have the required CSV file named "50_states.csv" containing the data of all 50 U.S. states. The CSV file should have columns for the state name, x-coordinate, and y-coordinate.

3. Run the Python script using your Python interpreter. For example, in the terminal or command prompt, navigate to the project directory and run:

   ```bash
   python your_script_name.py
   ```

4. The game will open a window with a blank map of the U.S. states.

5. You'll be prompted to guess the names of the U.S. states one by one. Type the name of a state and press Enter. If you guess correctly, the state's name will be displayed on the map, and your score will increase.

6. Keep guessing state names until you've guessed all 50 states or decide to exit the game.

7. If you want to exit the game at any time, type "Exit" when prompted for a state name. This will save the list of states you haven't guessed to a CSV file named "states_to_learn.csv" for future reference.

8. The game will exit when you've either guessed all 50 states or chosen to exit by typing "Exit."

## Game Mechanics
- The game keeps track of the number of correct guesses out of 50.
- If you exit the game early, it will save the list of states you still need to learn in a CSV file named "states_to_learn.csv" for you to review later.

## Data Source
The data for this game is loaded from the "50_states.csv" file, which should be in the same directory as the script. This CSV file contains information about the U.S. states' names and their corresponding coordinates.

## Screenshots


Enjoy playing and learning about the U.S. states!

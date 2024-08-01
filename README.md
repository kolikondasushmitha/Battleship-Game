Battleship Project
Overview
This project is a graphical implementation of the classic Battleship game using Python and Tkinter. Players can place their ships on a grid and take turns guessing the locations of the opponent's ships. The game supports both single-player (against the computer) and two-player modes.

Project Details
Name: Sushmitha Kolikonda

Features
Grid Setup: 10x10 grid for both player and computer.
Ship Placement: Players can place ships on their grid.
Turn-Based Gameplay: Players take turns guessing the locations of the opponent's ships.
Win/Loss Conditions: The game announces the winner once all ships of one player are sunk.
AI Opponent: Computer makes random guesses to find the player's ships.
Graphical Interface: Built using Tkinter, providing an interactive user experience.
How to Run
Ensure you have Python installed on your system.
Install Tkinter if not already installed.
Clone the repository.
Run the battleship.py script to start the game.
Code Structure
battleship.py: Main game logic and Tkinter interface.
battleship_tests.py: Test cases for different stages of the game.

Functions Overview
Stage 1
emptyGrid(rows, cols): Initializes an empty grid.
createShip(): Creates a ship of length 3.
checkShip(grid, ship): Checks if the ship can be placed on the grid.
addShips(grid, numShips): Adds ships to the grid.
Stage 2
isVertical(ship): Checks if a ship is placed vertically.
isHorizontal(ship): Checks if a ship is placed horizontally.
getClickedCell(data, event): Determines the cell clicked by the user.
drawShip(data, canvas, ship): Draws the ship on the user's grid.
shipIsValid(grid, ship): Validates the ship's placement.
placeShip(data): Places the ship on the user's grid.
clickUserBoard(data, row, col): Handles user clicks for placing ships.
Stage 3
updateBoard(data, board, row, col, player): Updates the board after a turn.
runGameTurn(data, row, col): Runs a game turn for both player and computer.
getComputerGuess(board): Generates a random guess for the computer.
isGameOver(board): Checks if the game is over.
drawGameOver(data, canvas): Displays the game over message.
Simulation Framework
The game uses a simulation framework to handle events and update the view. The main functions include:

updateView(data, userCanvas, compCanvas): Updates the game view.
keyEventHandler(data, userCanvas, compCanvas, event): Handles key events.
mouseEventHandler(data, userCanvas, compCanvas, event, board): Handles mouse events.
runSimulation(w, h): Initializes and runs the game simulation.
Tests
The project includes a set of tests for each stage of the game:

stage1Tests()
stage2Tests()
stage3Tests()
Getting Started
To get started, clone the repository and run the battleship.py script. Follow the instructions on the screen to place your ships and start playing.

Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

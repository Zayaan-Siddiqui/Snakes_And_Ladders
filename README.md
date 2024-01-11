## **Python Snakes and Ladders**

This project is a **Python implementation** of the classic board game "Snakes and Ladders". The game is designed to be played in a GUI using the **tkinter library**.

## **Features**

- Supports **2-4 players**
- **Randomly generates** the positions of snakes and ladders on the board.
- Players take turns to roll a dice and move their marker forward by the number rolled.
- If a player lands on a snake, they move back to the tail of the snake. If they land on a ladder, they move forward to the top of the ladder.
- The first player to reach the **100th square wins the game**.

## **Techniques and Skills**

1. **Object-Oriented Programming**: The game is structured around two main classes, `Player` and `Game`, demonstrating encapsulation and the use of instance methods.

2. **Graphical User Interface**: The game uses the tkinter library to create a graphical interface for the game. This includes creating buttons for each square on the board and for each player's dice roll.

3. **Randomness**: The `random` library is used to simulate dice rolls and to generate the positions of the snakes and ladders.

4. **Event-Driven Programming**: The game flow is controlled by events such as button clicks, demonstrating event-driven programming.

## **To run the game, follow these steps:**

- Ensure that **Python 3 and Tkinter** are installed on your machine. You can check this by running python --version and python -m tkinter in your terminal/command prompt. If Python and Tkinter are correctly installed, you should see your Python version and a small Tkinter window respectively.
- Clone the repository or download the Python file containing the game code.
- Open a terminal/command prompt and navigate to the directory containing the Python file.
- Run the command python filename.py, replacing “filename” with the name of the Python file.
- The game will prompt you to enter the number of players. Enter a number between 2 and 4, and the game will start.
- The current player can roll the dice by clicking their “Roll Dice” button. The game will automatically move the player’s piece and handle snakes and ladders. The first player to reach the 100th square wins the game.

# Tic-Tac-Toe-Game

This Tic Tac Toe Game is a GUI-based implementation of the classic two-player game, built using Python's tkinter library. It offers a simple and intuitive interface with a grid-based canvas for interaction, allowing players to alternate turns as "X" and "O" to compete for a win or draw.

## **1. Game Description**

The game is played on a 3x3 grid. Players take turns to mark one cell of the grid with their symbol ("X" or "O"). The goal is to form a horizontal, vertical, or diagonal line of three matching symbols. If all cells are filled without a winner, the game ends in a draw.

This application provides immediate visual feedback for each player's move, checks for win conditions after every turn, and displays the results through pop-up message boxes. At the end of a game, the board resets for a new match.

## **2. Functionalities**

### **Core Features**

**1. Interactive Grid:**

The 3x3 grid is drawn on a Canvas.
Players can click on cells to make their move.

**2. Player Symbols:**

Alternates between "X" and "O" as players take turns.
Symbols are drawn in the selected cell:
"X": Two intersecting lines in blue.
"O": A circle in red.

**3.Win Detection:**

Automatically checks all possible winning combinations:
Rows (3 horizontal lines).
Columns (3 vertical lines).
Diagonals (2 lines).
Declares a winner if a player achieves a matching line.

**4. Draw Detection:**

Declares a draw if all cells are filled without a winner.

**5. Game Reset:**

After a win or draw, the game automatically resets the board and starts a new round.

**6. Result Display:**

Uses messagebox to display:

"Player X wins!" or "Player O wins!" when a player wins.
"It's a draw!" when no winner is found.

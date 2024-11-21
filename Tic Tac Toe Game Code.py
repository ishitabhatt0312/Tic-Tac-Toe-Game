import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game state variables
board = [""] * 9  # A 3x3 board represented as a list
current_player = "X"  # X always starts

# Functions
def draw_board():
    """Draws the Tic Tac Toe grid on the canvas."""
    for i in range(1, 3):
        canvas.create_line(0, i * 100, 300, i * 100, width=2)  # Horizontal lines
        canvas.create_line(i * 100, 0, i * 100, 300, width=2)  # Vertical lines

def handle_click(event):
    """Handles the player's click to place X or O."""
    global current_player
    
    # Calculate the clicked cell
    x, y = event.x // 100, event.y // 100
    index = x + y * 3

    if board[index] == "":
        # Mark the cell
        board[index] = current_player
        draw_symbol(x, y, current_player)
        
        # Check for win or draw
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

def draw_symbol(x, y, player):
    """Draws X or O in the specified cell."""
    cx, cy = x * 100 + 50, y * 100 + 50
    if player == "X":
        canvas.create_line(cx - 30, cy - 30, cx + 30, cy + 30, width=4, fill="blue")
        canvas.create_line(cx - 30, cy + 30, cx + 30, cy - 30, width=4, fill="blue")
    elif player == "O":
        canvas.create_oval(cx - 30, cy - 30, cx + 30, cy + 30, width=4, outline="red")

def check_winner():
    """Checks if the current player has won."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return True
    return False

def reset_game():
    """Resets the game board and state."""
    global board, current_player
    board = [""] * 9
    current_player = "X"
    canvas.delete("all")
    draw_board()

# Create a canvas for the grid and symbols
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Draw the initial board
draw_board()

# Bind mouse click event
canvas.bind("<Button-1>", handle_click)

# Run the Tkinter main loop
root.mainloop()

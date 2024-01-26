import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for i in range(3):
        for j in range(3):
            button = tk.Button(root,
                            text=board[i][j], 
                            font=('italic', 20), 
                            width=26, 
                            height=6,
                            command=lambda row=i, col=j: on_button_click(row, col),
                            background="#FF00FF")
            
            
            button.grid(row=i, column=j)

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def on_button_click(row, col):
    global player_turn, board


    if board[row][col] == ' ' and player_turn:
        board[row][col] = 'X'
        print_board(board)
        
        if is_winner(board, 'X'):
            messagebox.showinfo("Game Over", "You won!")
            root.quit()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()

        player_turn = False
        computer_move()
    else:
        messagebox.showinfo("already marked", 'use only unmarked boxes')

def computer_move():
    global player_turn, board

    if not player_turn:
        comp_row, comp_col = best_move(board)
        board[comp_row][comp_col] = 'O'
        print_board(board)

        if is_winner(board, 'O'):
            messagebox.showinfo("Game Over", "Computer wins!")
            root.quit()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()

        player_turn = True

def best_move(board):
    best_val = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, False)
        board[i][j] = ' '
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
    return best_move

def minimax(board, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

root = tk.Tk()
root.title("Pragateesh Mani oowsi- min-max")
root.geometry("1920x1080")

player_turn = True
board = [[' ' for i in range(3)] for j in range(3)]

print_board(board)
root.mainloop()

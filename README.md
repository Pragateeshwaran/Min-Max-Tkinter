# Tic-Tac-Toe with Minimax Algorithm

This is a simple implementation of the classic Tic-Tac-Toe game in Python using the Tkinter library for the GUI. The computer player uses the Minimax algorithm to determine the best move.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository:

    ```bash
    git clone https://github.com/your-username/tic-tac-toe-minimax.git
    ```

3. Navigate to the project directory:

    ```bash
    cd tic-tac-toe-minimax
    ```

4. Run the script:

    ```bash
    python3 tic_tac_toe.py
    ```

## Features

- Human vs Computer gameplay.
- GUI developed using Tkinter.
- The computer player uses the Minimax algorithm for intelligent moves.

## Code Explanation

The code is well-commented and organized. Key functions include:

- `print_board(board)`: Display the Tic-Tac-Toe board.
- `is_winner(board, player)`: Check if a player has won.
- `is_full(board)`: Check if the board is full.
- `get_empty_cells(board)`: Get a list of empty cells on the board.
- `on_button_click(row, col)`: Handle the user's move.
- `computer_move()`: Execute the computer's move using the Minimax algorithm.
- `best_move(board)`: Determine the best move for the computer.
- `minimax(board, maximizing_player)`: Implement the Minimax algorithm.


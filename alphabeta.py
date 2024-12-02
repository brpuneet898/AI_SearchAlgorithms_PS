# Alpha-Beta Pruning Algorithm Implementation for Tic-Tac-Toe Game

# Constants for Tic-Tac-Toe game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to evaluate the board and return a score
def evaluate(board):
    # Check rows, columns, and diagonals for a winner
    for row in range(3):
        # Check rows
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return 10 if board[row][0] == PLAYER_X else -10

        # Check columns
        if board[0][row] == board[1][row] == board[2][row] != EMPTY:
            return 10 if board[0][row] == PLAYER_X else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == PLAYER_X else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == PLAYER_X else -10

    # If no winner, return 0 (neutral board)
    return 0

# Function to check if the game is over (either win or draw)
def is_game_over(board):
    return evaluate(board) != 0 or all(cell != EMPTY for row in board for cell in row)

# Alpha-Beta Pruning algorithm to find the best move
def alphabeta(board, depth, alpha, beta, is_max_player):
    score = evaluate(board)

    # If the maximizer has won, return the score
    if score == 10:
        return score - depth  # Subtract depth to prioritize quicker wins

    # If the minimizer has won, return the score
    if score == -10:
        return score + depth  # Add depth to prioritize quicker losses

    # If no more moves and it's a draw, return 0
    if is_game_over(board):
        return 0

    # Maximizer's turn (maximize the score)
    if is_max_player:
        best = -float('inf')

        # Loop through all possible moves for the maximizer
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X  # Make the move
                    best = max(best, alphabeta(board, depth + 1, alpha, beta, False))  # Minimize opponent's score
                    board[i][j] = EMPTY  # Undo the move

                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best

    # Minimizer's turn (minimize the score)
    else:
        best = float('inf')

        # Loop through all possible moves for the minimizer
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O  # Make the move
                    best = min(best, alphabeta(board, depth + 1, alpha, beta, True))  # Maximize player's score
                    board[i][j] = EMPTY  # Undo the move

                    beta = min(beta, best)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best

# Function to find the best move for the current player
def find_best_move(board):
    best_value = -float('inf')
    best_move = (-1, -1)

    # Loop through all possible moves and evaluate them
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X  # Make the move
                move_value = alphabeta(board, 0, -float('inf'), float('inf'), False)  # Minimize opponent's score
                board[i][j] = EMPTY  # Undo the move

                # If this move is better, update best move
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Example of how to use the Alpha-Beta Pruning algorithm to make a move

# Initialize a Tic-Tac-Toe board (empty)
board = [
    [PLAYER_X, PLAYER_O, EMPTY],
    [PLAYER_X, EMPTY, PLAYER_O],
    [EMPTY, EMPTY, PLAYER_X]
]

# Print the current board
print("Current Board:")
print_board(board)

# Find the best move for PLAYER_X (Maximizing player)
best_move = find_best_move(board)
print(f"\nBest move for {PLAYER_X} is at row {best_move[0]} and column {best_move[1]}")

# Make the move
board[best_move[0]][best_move[1]] = PLAYER_X

# Print the updated board
print("\nUpdated Board after the move:")
print_board(board)

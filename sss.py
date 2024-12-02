import random

# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to evaluate the board and return a score (simplified evaluation)
def evaluate(board):
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

    return 0  # Neutral if no winner

# Function to check if the game is over (either win or draw)
def is_game_over(board):
    return evaluate(board) != 0 or all(cell != EMPTY for row in board for cell in row)

# Function to simulate random outcomes for uncertainty (stochastic element)
def stochastic_simulation(board, is_max_player):
    possible_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
    if not possible_moves:
        return 0  # Draw (no available moves)
    
    move = random.choice(possible_moves)  # Randomly choose a move
    new_board = [row[:] for row in board]  # Copy the board
    if is_max_player:
        new_board[move[0]][move[1]] = PLAYER_X
    else:
        new_board[move[0]][move[1]] = PLAYER_O
    
    return evaluate(new_board)  # Return the evaluation after a random move

# SSS* Algorithm for adversarial search (simplified version)
def sss_star(board, depth, alpha, beta, is_max_player, max_simulations=10):
    if is_game_over(board) or depth >= max_simulations:
        return evaluate(board)

    # Stochastic simulations for each possible move
    best_value = -float('inf') if is_max_player else float('inf')

    possible_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
    
    for move in possible_moves:
        new_board = [row[:] for row in board]  # Create a copy of the board
        if is_max_player:
            new_board[move[0]][move[1]] = PLAYER_X
        else:
            new_board[move[0]][move[1]] = PLAYER_O

        # Simulate random outcomes (Stochastic Simulation)
        simulation_results = [stochastic_simulation(new_board, not is_max_player) for _ in range(max_simulations)]
        avg_result = sum(simulation_results) / len(simulation_results)  # Average of simulations

        if is_max_player:
            best_value = max(best_value, avg_result)
            alpha = max(alpha, best_value)
        else:
            best_value = min(best_value, avg_result)
            beta = min(beta, best_value)

        if beta <= alpha:
            break  # Pruning: No need to search further

    return best_value

# Function to find the best move using the SSS* algorithm
def find_best_move(board, max_simulations=10):
    best_value = -float('inf')
    best_move = (-1, -1)

    # Loop through all possible moves and evaluate them
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X  # Make the move
                move_value = sss_star(board, 0, -float('inf'), float('inf'), False, max_simulations)
                board[i][j] = EMPTY  # Undo the move

                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Example of how to use the SSS* algorithm to make a move

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

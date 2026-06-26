# Tic Tac Toe Game in Python (Console Version)

def print_board(board):
    """Display the current game board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    """Check if the given player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full (draw)."""
    return all(cell != " " for row in board for cell in row)

def get_move(player, board):
    """Get a valid move from the player."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column: 1 1 for top-left): ")
            row, col = map(int, move.split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid position! Enter numbers between 1 and 3.")
                continue
            if board[row - 1][col - 1] != " ":
                print("That spot is already taken! Try again.")
                continue
            return row - 1, col - 1
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")

def tic_tac_toe():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

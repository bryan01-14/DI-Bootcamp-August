"""TicTacToe - Two player game."""




EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

WINNING_COMBINATIONS = [
    # Rows
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # Columns
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # Diagonals
    [0, 4, 8],
    [2, 4, 6],
]



def create_board():
    """Create and return a fresh empty board (list of 9 empty strings)."""
    return [EMPTY] * 9


def display_board(board):
    """
    Display the current state of the board.
    Positions are numbered 1-9 for user reference.

    Visual layout:
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
    """
    print("\n")
    print(f"  {board[0]} | {board[1]} | {board[2]}       7 | 8 | 9")
    print("  --+---+--       --+---+--")
    print(f"  {board[3]} | {board[4]} | {board[5]}       4 | 5 | 6")
    print("  --+---+--       --+---+--")
    print(f"  {board[6]} | {board[7]} | {board[8]}       1 | 2 | 3")
    print("\n")




def player_input(board, player):
    """
    Ask the current player to choose a position (1-9).
    Keeps asking until a valid and empty cell is chosen.
    Returns the chosen index (0-based).
    """
    while True:
        try:
            position = int(input(f"  Player {player}, choose a position (1-9): "))
            if position < 1 or position > 9:
                print("   Invalid position. Please choose a number between 1 and 9.")
                continue
            index = position - 1  # Convert to 0-based index
            if board[index] != EMPTY:
                print(f"   Position {position} is already taken. Choose another.")
                continue
            return index
        except ValueError:
            print("   Please enter a valid number between 1 and 9.")




def place_mark(board, index, player):
    """Place the player's mark on the board at the given index."""
    board[index] = player


def check_win(board, player):
    """
    Check if the given player has won.
    Returns True if the player has 3 marks in a row, column, or diagonal.
    """
    for combo in WINNING_COMBINATIONS:
        if all(board[i] == player for i in combo):
            return True
    return False


def check_draw(board):
    """Return True if the board is full and no winner (draw)."""
    return all(cell != EMPTY for cell in board)


def switch_player(current_player):
    """Switch and return the other player."""
    return PLAYER_O if current_player == PLAYER_X else PLAYER_X




def display_welcome():
    """Display the welcome message."""
    print("\n" + "=" * 40)
    print("         TIC TAC TOE 🎮")
    print("=" * 40)
    print("  Player 1 = X  |  Player 2 = O")
    print("  Choose a position from 1 to 9")
    print("=" * 40)


def display_winner(player):
    """Display the winner message."""
    print("=" * 40)
    print(f"   Player {player} wins! Congratulations!")
    print("=" * 40)


def display_draw():
    """Display the draw message."""
    print("=" * 40)
    print("   It's a draw! Well played both!")
    print("=" * 40)


def ask_play_again():
    """
    Ask the players if they want to play again.
    Returns True if yes, False if no.
    """
    while True:
        choice = input("\n  Play again? (y / n): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("   Please enter 'y' or 'n'.")



def display_scores(scores):
    """Display the current scores for both players."""
    print("\n  --- Scores ---")
    print(f"  Player X : {scores[PLAYER_X]} win(s)")
    print(f"  Player O : {scores[PLAYER_O]} win(s)")
    print(f"  Draws    : {scores['draw']}")
    print("  --------------")




def play():
    """
    Main function to run the TicTacToe game.
    Handles the game loop, player turns, win/draw detection,
    score tracking, and play-again prompt.
    """
    display_welcome()

    # Score tracker
    scores = {PLAYER_X: 0, PLAYER_O: 0, "draw": 0}

    while True:
        # Setup a new game
        board = create_board()
        current_player = PLAYER_X  # X always starts

        print(f"\n   New game! Player {current_player} goes first.")

        # Game loop for one round
        while True:
            display_board(board)

            # Get player's move
            index = player_input(board, current_player)
            place_mark(board, index, current_player)

            # Check for win
            if check_win(board, current_player):
                display_board(board)
                display_winner(current_player)
                scores[current_player] += 1
                break

            # Check for draw
            if check_draw(board):
                display_board(board)
                display_draw()
                scores["draw"] += 1
                break

            # Switch player
            current_player = switch_player(current_player)

        # Show scores after each round
        display_scores(scores)

        # Ask to play again
        if not ask_play_again():
            print("\n  Thanks for playing TicTacToe! Goodbye! ")
            print("=" * 40)
            break


if __name__ == "__main__":
    play()
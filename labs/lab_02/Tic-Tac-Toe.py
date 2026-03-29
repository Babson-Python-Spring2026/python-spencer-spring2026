"""
TIC TAC TOE — FUNCTION SCAFFOLD

Board Representation Rules:
- Board is a list of 9 integers.
- 1-9  → open squares
- 10   → X
- -10  → O

Winning rule:
- Any row, column, or diagonal that sums to:
    30   → X wins
   -30   → O wins


Assume:
- X plays first
- X is human
- O is computer
"""

import random
import os


def create_board() -> list[int]:
    """
    Create and return a new Tic-Tac-Toe board.

    Returns:
        A list containing the numbers 1 through 9.
    """
    return list(range(1, 10))


def display_board(board: list[int]) -> None:
    """
    Display the Tic-Tac-Toe board in a 3x3 format.

    Requirements:
    - Show X for value 10
    - Show O for value -10
    - Show the square number (1-9) for open squares
    - Format the board clearly with rows and separators
    """
    def cell(value: int) -> str:
        if value == 10: return 'X'
        elif value == -10: return 'O'
        else: return str(value)

    print()

    for row in range(3):
        row_values = [cell(board[row * 3 + col]) for col in range(3)]
        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        if row < 2:
            print('-----------')
    print()


def check_tie(board: list[int]) -> bool:
    """
    Determine whether the board is full.

    Returns:
        True  → if no open squares remain
        False → otherwise
    """
    # go through each cell, if any still has a number 1-9 theres room left
    for cell in board:
        if cell >= 1 and cell <= 9:
            return False
    return True


def check_winner(board: list[int]) -> str | None:
    """
    Determine if a player has won.

    Requirements:
    - Check all rows
    - Check all columns
    - Check both diagonals
    - Use the board sum rule (30 / -30)

    Returns:
        'X', 'O', or None
    """
    # all 8 winning combos
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]

    for a, b, c in lines:
        total = board[a] + board[b] + board[c]
        if total == 30:
            return 'X'
        elif total == -30:
            return 'O'
    return None


def game_over(board: list[int], x_moves: bool) -> str | None:
    """
    Determine if the game has ended.

    Rules:
    - If a player has won, return 'X' or 'O'
    - If the board is full and no winner, return 'TIE'
    - Otherwise return None
    """
    winner = check_winner(board)
    if winner:
        return winner

    if check_tie(board):
        return 'TIE'

    return None


def get_human_move(board: list[int]) -> str:
    """
    Prompt the human player to select a square.

    Returns:
        The raw input string entered by the user.
    """
    return input("Your move (1-9): ")


def get_computer_move(board: list[int]) -> int:
    """
    Determine the computer's move.

    Requirements:
    - Select an open square.
    - Randomly picks from available open squares.

    Returns:
        An integer representing the chosen square number.
    """
    open_squares = [cell for cell in board if cell not in (10, -10)]
    return random.choice(open_squares)


def is_valid_move(board: list[int], move: str) -> tuple[bool, int | None]:
    """
    Validate a player's move.

    Steps:
    - Convert input to integer.
    - Ensure it is between 1 and 9.
    - Ensure the square is not already taken.

    Returns:
        (True, move_int)  → if valid (1-based square number)
        (False, None)     → otherwise
    """
    try:
        num = int(move)
    except ValueError:
        return (False, None)

    if num < 1 or num > 9:
        return (False, None)

    # check if the square is already taken
    if board[num - 1] == 10 or board[num - 1] == -10:
        return (False, None)

    return (True, num)


def place_move(board: list[int], index: int, x_moves: bool) -> None:
    """
    Place a move on the board.

    Rules:
    - If x_moves is True, place 10
    - If x_moves is False, place -10
    - Modify the board in place
    - index is 1-based (square number), convert to 0-based
    """
    board[index - 1] = 10 if x_moves else -10


def play_game() -> None:
    """
    Run the full Tic-Tac-Toe game loop.
    """
    board = create_board()
    x_moves = True

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(board)

        if x_moves:
            move = get_human_move(board)
        else:
            print("Computer is thinking...")
            move = str(get_computer_move(board))

        valid, square = is_valid_move(board, move)

        if not valid:
            print("Invalid move, try again.")
            input("Press enter to continue...")
            continue

        if not x_moves:
            print(f"Computer picks {square}")

        place_move(board, square, x_moves)

        result = game_over(board, x_moves)
        if result:
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(board)
            if result == 'TIE':
                print("It's a tie!")
            else:
                print(f"{result} wins!")
            break

        x_moves = not x_moves


if __name__ == "__main__":
    play_game()

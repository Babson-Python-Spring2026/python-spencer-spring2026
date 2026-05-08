

"""
TIC TAC TOE - FUNCTION SCAFFOLD

Lab 2 (tictactoe) is due Monday March 9th, 2026

Board Representation Rules:
- Board is a list of 9 integers.
- 1-9  ? open squares
- 10   ? X
- -10  ? O

Winning rule:
- Any row, column, or diagonal that sums to:
    30   ? X wins
   -30   ? O wins


Assume:
- X plays first
- X is human
-O is computer
"""
import os
def clear_screen():
    # only works in py files    
    os.system("cls" if os.name == "nt" else "clear")

import time
def pause(n=None):
    if n is None:
        input("Press Enter to continue...")
    else:
        time.sleep(n)

def create_board() -> list[int]:
    """
    Create and return a new Tic-Tac-Toe board.

    Returns:
        A list containing the numbers 1 through 9.
    """
    
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]



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
        row_values = []
        for col in range(3):
            value = cell(board[row * 3 + col])
            row_values.append(value)

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
        True  ? if no open squares remain
        False ? otherwise
    """

    for space in board:
        if space >= 1 and space <= 9:
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
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    
    for a, b, c in winning_combinations:
        total = board[a] + board[b] + board[c]
        
        if total == 30:
            return 'X'
        elif total == -30:
            return 'O'
    
    return None



def game_over(board: list[int]) -> str | None:
    """
    Determine if the game has ended.

    Rules:
    - If a player has won, return 'X' or 'O'
    - If the board is full and no winner, return 'TIE'
    - Otherwise return None
    - function should call both check_winner() and check_tie()
    """

    winner = check_winner(board)

    if winner is not None:
        return winner

    if check_tie(board):
        return 'TIE'

    return None




def get_human_move() -> str:
    """
    Prompt the human player to select a square.

    Returns:
        The raw input string entered by the user.
    """
    move = input("Choose a square (1-9): ")
    return move
    


import random
def get_computer_move(board: list[int]) -> int:
    """
    Determine the computer's move.

    Requirements:
    - Select an open square.
    - For now, may choose the first available open square.
    - or, choose random open square

    Returns:
        An integer representing the chosen square number.
    """

    open_squares = []
    for space in board:
        if space >= 1 and space <= 9:
            open_squares.append(space)    

    return random.choice(open_squares)


def is_valid_move(board: list[int], move: str) -> tuple[bool, int | None]:
    """
    Validate a player's move.

    Steps:
    - Convert input to integer.
    - Ensure it is between 1 and 9.
    - Ensure the square is not already taken.

    Returns:
        (True, index)  ? if valid
        (False, None)  ? otherwise
    """
    try:
        move_int = int(move)
    except ValueError:
        return (False, None)

    if move_int < 1 or move_int > 9:
        return (False, None)

    index = move_int - 1

    if board[index] == 10 or board[index] == -10:
        return (False, None)

    return (True, index)
    


def place_move(board: list[int], index: int, x_moves: bool) -> None:
    """
    Place a move on the board.

    Rules:
    - If x_moves is True, place 10
    - If x_moves is False, place -10
    - Modify the board in place
    """

    if x_moves:
        board[index] = 10
    else:
        board[index] = -10
    

def play_game() -> None:
    """
    Run the full Tic-Tac-Toe game loop.

    Responsibilities:
    - Create a fresh board using create_board()
    - Track whose turn it is (X goes first)
    - Loop until the game ends:
        - Clear the screen (optional, if you have a helper)
        - Display the board each turn
        - If it is X's turn:
            - Get human input via get_human_move()
          Else:
            - Get computer move via get_computer_move(board)
        - Validate the move using is_valid_move(board, move)
            - If invalid: show an error message (if your validator doesn't) and continue
        - Apply the move using place_move(board, index, x_moves)
        - Check for end-of-game using game_over(board)
            - If it returns 'X' or 'O': announce winner and stop
            - If it returns 'TIE': announce tie and stop
        - Switch turns (toggle x_moves)

    Output:
    - Prints the game progression and final result to the console.
    """
    board = create_board()
    x_moves = True

    while True:
        clear_screen()
        display_board(board)

        if x_moves:
            move = get_human_move()
        else:
            print("Computer thinking...")
            pause(1)
            move = str(get_computer_move(board))

        is_valid = is_valid_move(board, move)

        if not is_valid[0]:
            print("Invalid move. Try again.")
            continue

        place_move(board, is_valid[1], x_moves)

        status = game_over(board)

        if status:
            clear_screen()
            display_board(board)

            if status == "TIE":
                print("The game is a tie.")
            else:
                print(status + " wins the game")

            break

        x_moves = not x_moves
    
play_game()
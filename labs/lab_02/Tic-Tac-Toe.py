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

NOTE: I had the helper functions done in a separate file (tictactoe_lab.py) 
and didnt realize I was supposed to put everything in THIS file. My bad.
Moving everything over now.
"""


def create_board() -> list[int]:
    """
    Create and return a new Tic-Tac-Toe board.

    Returns:
        A list containing the numbers 1 through 9.
    """
    # just returns numbers 1-9 for the starting board
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
    # helper to convert the number to X, O, or the square number
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
    # if any cell still has 1-9 in it, board isnt full yet
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
    # all 8 winning lines - rows, columns, diagonals
    lines = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left col
        [1, 4, 7],  # middle col
        [2, 5, 8],  # right col
        [0, 4, 8],  # diagonal top-left to bottom-right
        [2, 4, 6]   # diagonal top-right to bottom-left
    ]
    
    # check each line - if sum is 30 its X, if -30 its O
    for line in lines:
        total = board[line[0]] + board[line[1]] + board[line[2]]
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
    # first check if someone won
    winner = check_winner(board)
    if winner:
        return winner
    
    # if no winner but board is full, its a tie
    if check_tie(board):
        return 'TIE'
    
    # game still going
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
    - For now, may choose the first available open square.

    Returns:
        An integer representing the chosen square number.
    """
    # just pick the first open square, nothing fancy
    for i in range(9):
        if board[i] >= 1 and board[i] <= 9:
            return board[i]
    return -1  # shouldnt happen but just in case


def is_valid_move(board: list[int], move: str) -> tuple[bool, int | None]:
    """
    Validate a player's move.

    Steps:
    - Convert input to integer.
    - Ensure it is between 1 and 9.
    - Ensure the square is not already taken.

    Returns:
        (True, index)  → if valid
        (False, None)  → otherwise
    """
    # try to convert to int
    try:
        num = int(move)
    except ValueError:
        return (False, None)
    
    # check if its in range
    if num < 1 or num > 9:
        return (False, None)
    
    # check if square is taken (10 or -10 means X or O is there)
    index = num - 1
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
        board[index] = 10   # X
    else:
        board[index] = -10  # O


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
            - Get human input via get_human_move(board)
          Else:
            - Get computer move via get_computer_move(board)
        - Validate the move using is_valid_move(board, move)
            - If invalid: show an error message (if your validator doesn't) and continue
        - Apply the move using place_move(board, index, x_moves)
        - Check for end-of-game using game_over(board, x_moves)
            - If it returns 'X' or 'O': announce winner and stop
            - If it returns 'TIE': announce tie and stop
        - Switch turns (toggle x_moves)

    Output:
    - Prints the game progression and final result to the console.
    """
    board = create_board()
    x_moves = True  # X goes first
    
    while True:
        display_board(board)
        
        if x_moves:
            # human turn
            print("X's turn (You)")
            move = get_human_move(board)
            valid, index = is_valid_move(board, move)
            if not valid:
                print("Invalid move, try again.")
                continue
        else:
            # computer turn
            print("O's turn (Computer)")
            move_num = get_computer_move(board)
            valid, index = is_valid_move(board, str(move_num))
            print(f"Computer picks {move_num}")
        
        # place the move on the board
        place_move(board, index, x_moves)
        
        # check if game ended
        result = game_over(board, x_moves)
        if result == 'X':
            display_board(board)
            print("X wins!")
            break
        elif result == 'O':
            display_board(board)
            print("O wins!")
            break
        elif result == 'TIE':
            display_board(board)
            print("It's a tie!")
            break
        
        # switch turns
        x_moves = not x_moves


if __name__ == "__main__":
    play_game()

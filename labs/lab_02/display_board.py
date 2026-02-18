from utils.functions import clear_screen

def display_board(board: list[int]) -> None:
    """
    Display the Tic-Tac-Toe board.
    Args:
        board: List of 9 integers (10 for X, -10 for O, 1-9 for open).
    """
    def cell(value: int) -> str:
        if value == 10: return 'X'
        elif value == -10: return 'O'
        else: return str(value)

    clear_screen()
    print()

    for row in range(3):
        row_values = [cell(board[row * 3 + col]) for col in range(3)]
        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        if row < 2:
            print('-----------')
    print()

board = [10,2,3,4,5,6,7,8,-10]
display_board(board)

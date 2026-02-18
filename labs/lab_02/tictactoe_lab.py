# Lab 2 - TicTacToe
# board is a 9-element list
# 1-9 means open, 10 means X, -10 means O
# winning = row/col/diagonal sums to 30 (X) or -30 (O)


def board_full(board):
    """
    Returns True if no empty spaces left.
    Returns False otherwise.
    """
    for cell in board:
        if cell >= 1 and cell <= 9:
            return False
    return True


def check_winner(board):
    """
    Returns 'X' if X won, 'O' if O won, None otherwise.
    """
    # the 8 ways to win
    lines = [
        [0, 1, 2],  # rows
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # cols
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # diagonals
        [2, 4, 6]
    ]
    
    for line in lines:
        total = board[line[0]] + board[line[1]] + board[line[2]]
        if total == 30:
            return 'X'
        elif total == -30:
            return 'O'
    return None


def game_over(board):
    """
    Returns 'X' or 'O' if winner, 'TIE' if full, None if still playing.
    """
    winner = check_winner(board)
    if winner:
        return winner
    
    if board_full(board):
        return 'TIE'
    
    return None

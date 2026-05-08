# replay.py — replays a saved tic tac toe game from last_game.json
# reads the move history and rebuilds the board one move at a time

import json
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def create_board():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board(board):
    # same display function from the main game
    def cell(value):
        if value == 10: return 'X'
        elif value == -10: return 'O'
        else: return str(value)

    print()
    for row in range(3):
        row_values = []
        for col in range(3):
            row_values.append(cell(board[row * 3 + col]))

        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        if row < 2:
            print('-----------')
    print()


def place_move(board, square, x_moves):
    # square is 1-based, convert to 0-based index
    # transition: places X (10) or O (-10) onto the board
    board[square - 1] = 10 if x_moves else -10


def replay_game():
    # load the saved game data from json
    load_path = os.path.join(os.path.dirname(__file__), "last_game.json")

    with open(load_path, "r") as f:
        game_data = json.load(f)

    # state: moves is the full history, result is how the game ended
    moves = game_data["moves"]
    result = game_data["result"]

    print(f"Replaying game with {len(moves)} moves. Result: {result}")
    print("Press Enter to step through each move.\n")

    # start with a fresh board — same starting state as the original game
    board = create_board()

    # show the empty board first
    display_board(board)
    input("Press Enter to see move 1...")

    # replay each move one at a time
    for i in range(len(moves)):
        # invariant: even index = X's turn, odd index = O's turn (X always goes first)
        x_turn = (i % 2 == 0)
        player = "X" if x_turn else "O"

        # transition: place the move on the board
        place_move(board, moves[i], x_turn)

        clear_screen()
        print(f"Move {i + 1}: {player} plays square {moves[i]}")
        display_board(board)

        # if there are more moves, wait for enter
        if i < len(moves) - 1:
            input("Press Enter for next move...")

    # show the final result
    print()
    if result == "TIE":
        print("Game ended in a tie.")
    else:
        print(f"{result} wins the game!")


replay_game()

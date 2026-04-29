import random
import os


HIDDEN = "♦"
MINE = "💣"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_int(prompt, low, high):
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
            if low <= value <= high:
                return value
        except ValueError:
            pass


def place_mines(height, width, count):
    """Pick random cells for mines, return as a set of (row, col)."""
    all_cells = []
    for r in range(height):
        for c in range(width):
            all_cells.append((r, c))

    return set(random.sample(all_cells, count))


def count_neighbors(row, col, height, width, mines):
    """Count how many of the 8 neighbors are mines."""
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < height and 0 <= nc < width:
                if (nr, nc) in mines:
                    total += 1
    return total


def build_number_board(height, width, mines):
    """Build a 2d list where each cell is the count of neighboring mines."""
    board = []
    for r in range(height):
        row = []
        for c in range(width):
            if (r, c) in mines:
                row.append(-1)
            else:
                row.append(count_neighbors(r, c, height, width, mines))
        board.append(row)
    return board


def print_board(number_board, revealed, mines, show_all=False):
    clear_screen()
    height = len(number_board)
    width = len(number_board[0])

    # column headers
    print("   ", end="")
    for c in range(width):
        print(f" {c:^3}", end="")
    print()

    divider = "   " + " ---" * width
    print(divider)

    for r in range(height):
        print(f" {r} |", end="")
        for c in range(width):
            if show_all and (r, c) in mines:
                print(f" {MINE} |", end="")
            elif (r, c) in revealed:
                val = number_board[r][c]
                display = " " if val == 0 else str(val)
                print(f" {display}  |", end="")
            else:
                print(f" {HIDDEN}  |", end="")
        print()
        print(divider)
    print()


def play():
    height = get_int("Board height (2 - 10) : ", 2, 10)
    width = get_int("Board width (2 - 10) : ", 2, 10)

    max_mines = height * width
    mine_count = get_int(f"How many mines (less then {max_mines}) : ", 1, max_mines - 1)

    mines = place_mines(height, width, mine_count)
    number_board = build_number_board(height, width, mines)
    revealed = set()

    safe_total = height * width - mine_count

    while True:
        print_board(number_board, revealed, mines)

        over = get_int("How many over would you like to dig? : ", 0, width - 1)
        down = get_int("How many down would you like to dig? : ", 0, height - 1)

        if (down, over) in revealed:
            continue

        # hit a mine
        if (down, over) in mines:
            print_board(number_board, revealed, mines, show_all=True)
            print("Boom! You hit a mine.")
            break

        # safe dig
        revealed.add((down, over))

        # check win
        if len(revealed) == safe_total:
            print_board(number_board, revealed, mines, show_all=True)
            print("You cleared the board. You win!")
            break


play()

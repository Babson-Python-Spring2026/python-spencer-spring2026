'''
Spencer — Grade: 9 / 10
Overall evaluation

This is a very strong submission. Spencer clearly understands the core computational ideas behind the program: the shared board state, the role of undoing moves, and the use of canonical board representations to remove symmetry duplicates. The explanations are clear, structured, and show real reasoning about how the program works.

The student also completed all required tasks: defining state, identifying transitions and invariants, replacing TODO docstrings, adding inline comments, explaining a non-obvious part of the program, and interpreting the output.

Strengths
1. Clear definition of state

The student correctly identifies the major state variables, including the board, counters, and the list of unique terminal boards.

They also correctly recognize that the loop variables represent part of the search state.

This shows good understanding of how the algorithm explores the game tree.

2. Good explanation of transitions

Spencer correctly identifies transitions in:

the nested loops when moves are placed
undo operations
functions that update counters and lists

This demonstrates understanding that transitions occur both in the search loops and in helper functions.

3. Strong invariant reasoning

The invariants identified are appropriate:

search stops after a win
players alternate turns
moves only placed on empty squares
unique boards stored in canonical form

These are exactly the structural properties that keep the search valid.

4. Excellent explanation of undoing moves

The explanation of backtracking is particularly strong.

The student recognizes that:

there is only one board object
moves must be undone to explore different branches
otherwise previous moves would remain on the board

The analogy of erasing moves on paper is a very clear explanation of the concept.

This is the key conceptual idea in the assignment, and the student explains it well.

5. Accurate interpretation of program output

The explanation of the output numbers is correct:

total full boards
number of unique terminal boards
counts of wins and draws
unique board shapes

This indicates that the student understood what the counters represent.

GRADE 95

'''

"""
Homework: Reading Code with State / Transitions / Invariants (Tic-Tac-Toe)

This program brute-forces tic-tac-toe WITHOUT recursion.

What it actually counts:
- It explores all possible games where X starts and players alternate.
- The search STOPS as soon as someone wins (a terminal state).
- It also records full boards that end in a tie.
- It tracks UNIQUE *terminal* boards "up to symmetry" (rotations + reflections),
  meaning rotated/flipped versions are treated as the same terminal board.

---

YOUR TASKS:

RULE:  Do not change any executable code (no reformatting logic, no renaming variables, no moving lines). 
       Only add/replace comments and docstrings.
       
1) Define STATE for this program.
   - What variables change as the program runs?
   
   STATE VARIABLES:
   - board: the current game state (9-element list showing X, O, or empty for each square)
   - unique_seen: list of all unique terminal board configurations weve found (in standard form)
   - full_boards: count of games that went all 9 moves
   - x_wins, o_wins, ties: counts of unique terminal boards by outcome
   - x_wins_on_full_board, draws_on_full_board: subset counts for 9-move games
   - the loop variables (x1, o1, x2, etc): which squares were chosen at each move
   
2) Explain where TRANSITIONS happen.
   - Where does the state change? (where in the code, which functions)
   
   TRANSITIONS HAPPEN:
   - In the nested loops when we do board[x1] = 'X' or board[o1] = 'O' etc
   - In record_unique_board() when we append to unique_seen and increment counters
   - In record_full_board() when we increment full_boards and related counters
   - When we undo moves: board[x1] = ' ' etc (transition back to previous state)
   
3) Identify 4 INVARIANTS.
   - What properties remain true as the program runs (and what checks enforce them).
   - For instance: has_winner() is a check; the invariant is "we do not continue exploring after a win."
   
   INVARIANT 1: We never continue exploring after a win
   - has_winner() checks for this, should_continue() returns False if someone won
   - This means we stop the search branch as soon as theres a winner
   
   INVARIANT 2: X always moves on odd turns, O on even turns
   - Enforced by the loop structure itself - x1 is move 1, o1 is move 2, etc
   - We never check this explicitly but the nested loop order guarantees it
   
   INVARIANT 3: We only place moves on empty squares
   - Each inner loop checks "if board[pos] == ' '" before placing a piece
   - This prevents overwriting existing moves
   
   INVARIANT 4: Each board in unique_seen is in "standard form" (canonical representation)
   - standard_form() computes the canonical version before checking/adding
   - This ensures we dont count rotations or reflections as different boards
   
4) For every function that says ''' TODO ''', replace that docstring with a real explanation
   of what the function does (1-4 sentences).
5) Add inline comments anywhere you see "# TODO" explaining what that code block is doing.
6) DO NOT USE AI. Write 5-8 sentences explaining one non-obvious part (choose one):  
   (a) symmetry logic (what makes a board unique), 
   (b) why we undo moves, 
   (c) why standard_form() produces uniqueness

   EXPLANATION - Why we undo moves:
   
   So theres only one board in memory. One list. Every game we explore uses that same list.
   When X picks square 0 and we play out all the games from there, we need to clear square 0 
   before trying square 1. Otherwise the board still has an X sitting in square 0 from before.
   
   I kept getting confused by this at first. Like why not just make a new board each time? 
   But then youd have millions of lists. This way you reuse the same one and just clean up 
   after yourself. Put a piece down, explore everything, pick it back up.
   
   Its like if you were drawing out games on paper but erasing instead of getting a new sheet 
   every time. The undo lines at the bottom of each loop are the eraser.
   
7) The output from the program is two print statements:
       127872
       138 81792 46080 91 44 3

    explain what each number represents.
    
    OUTPUT EXPLANATION:
    - 127872: total number of full boards (games that went all 9 moves without earlier win)
    - 138: number of unique terminal boards (counting symmetrical boards as one)
    - 81792: number of full boards where X won on the 9th move
    - 46080: number of full boards that ended in a draw
    - 91: unique terminal boards where X won
    - 44: unique terminal boards where O won  
    - 3: unique terminal boards that were ties


Submission:
- Update this file with your answers. Commit and sync

"""

# ----------------------------
# Global running totals (STATE)
# ----------------------------

unique_seen = []             # stores the "standard form" of each unique terminal board weve encountered
                             # we use standard forms so rotations/reflections arent counted separately
board = [' '] * 9            # the current game board - 9 squares, ' ' means empty
                             # we reuse this one list for all games, undoing moves as we backtrack

full_boards = 0              # counts games that used all 9 squares (no early winner)
x_wins_on_full_board = 0     # subset of full_boards where X won on move 9
draws_on_full_board = 0      # subset of full_boards that ended in a tie (no winner)

x_wins = 0                   # count of unique terminal boards where X won
o_wins = 0                   # count of unique terminal boards where O won
ties = 0                     # count of unique terminal boards that were ties


# ----------------------------
# Board representation helpers
# ----------------------------

def to_grid(flat_board: list[str]) -> list[list[str]]:
    '''
    Takes the flat 9-element list and makes it a 3x3 grid.
    Easier to rotate and flip when its in grid form.
    '''
    grid = []
    for row in range(3):
        row_vals = []
        for col in range(3):
            row_vals.append(flat_board[row * 3 + col])
        grid.append(row_vals)
    return grid


def rotate_clockwise(grid: list[list[str]]) -> list[list[str]]:
    '''
    Rotates the grid 90 degrees clockwise. Pretty standard rotation logic.
    '''
    rotated = [[' '] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            rotated[c][2 - r] = grid[r][c]
    return rotated


def flip_vertical(grid: list[list[str]]) -> list[list[str]]:
    '''
    Flips top to bottom. Row 0 becomes row 2, row 2 becomes row 0.
    '''
    return [grid[2], grid[1], grid[0]]


def standard_form(flat_board: list[str]) -> list[list[str]]:
    '''
    Gets the "canonical" version of a board. Makes all 8 versions (4 rotations, 
    plus flipped versions of each) and returns whichever one is smallest when 
    you compare them. So if two boards are just rotations of each other theyll 
    both return the same standard form.
    '''
    grid = to_grid(flat_board)
    flipped = flip_vertical(grid)

    variants = []
    for _ in range(4):
        variants.append(grid)
        variants.append(flipped)
        grid = rotate_clockwise(grid)
        flipped = rotate_clockwise(flipped)

    return min(variants)


def record_unique_board(flat_board: list[str]) -> None:
    '''
    Checks if weve seen this board before. If not, adds it to unique_seen and 
    bumps the right counter (x_wins, o_wins, or ties). Uses standard_form so 
    rotations dont get counted twice.
    '''
    global x_wins, o_wins, ties

    rep = standard_form(flat_board)

    # only add to our list if we havent seen this configuration before
    # this is how we avoid counting rotations/reflections multiple times
    if rep not in unique_seen:
        unique_seen.append(rep)

        # figure out who won (or if its a tie) and update the right counter
        winner = who_won(flat_board)
        if winner == 'X':
            x_wins += 1
        elif winner == 'O':
            o_wins += 1
        else:
            ties += 1


# ----------------------------
# Game logic
# ----------------------------

def has_winner(flat_board: list[str]) -> bool:
    '''
    Checks all 8 winning lines (3 rows, 3 cols, 2 diagonals). Uses a scoring 
    thing where X is +10 and O is -10, so three Xs in a row = 30, three Os = -30.
    Returns True if anyone won, False otherwise.
    '''
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [6, 4, 2],             # diagonals
    ]

    for line in winning_lines:
        score = 0
        for idx in line:
            if flat_board[idx] == 'X':
                score += 10
            elif flat_board[idx] == 'O':
                score -= 10
        if abs(score) == 30:
            return True

    return False


def who_won(flat_board: list[str]) -> str:
    '''
    Same idea as has_winner but tells you WHO won instead of just yes/no.
    Returns 'X', 'O', or 'TIE'.
    '''
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [6, 4, 2],             # diagonals
    ]

    for line in winning_lines:
        score = 0
        for idx in line:
            if flat_board[idx] == 'X':
                score += 10
            elif flat_board[idx] == 'O':
                score -= 10

        if score == 30:
            return 'X'
        elif score == -30:
            return 'O'

    return 'TIE'


def should_continue(flat_board: list[str], move_number: int) -> bool:
    '''
    Should we keep going or stop? If someone already won, stop and record it.
    No point playing more moves after the games over.
    '''
    # if theres a winner, record this board and stop exploring this branch
    if has_winner(flat_board):
        record_unique_board(flat_board)
        return False
    return True


def record_full_board(flat_board: list[str]) -> None:
    '''
    Called when we hit move 9 and the board is full. Records it and bumps 
    the full_boards count. Also figures out if X won on that last move or 
    if its a draw.
    '''
    global full_boards, x_wins_on_full_board, draws_on_full_board

    # this is definitely a terminal state since the board is completely full
    record_unique_board(flat_board)
    full_boards += 1

    # on a full board, either X just won with move 9, or nobody won (draw)
    if has_winner(flat_board):
        x_wins_on_full_board += 1
    else:
        draws_on_full_board += 1


# ----------------------------
# Brute force search (9 nested loops)
# ----------------------------

# TRANSITIONS happen in two places in these loops:
# 1. When we place a piece: board[x1] = 'X' (or 'O')
# 2. When we undo a piece: board[x1] = ' '
# 
# Other transitions happen in the helper functions:
# - record_unique_board updates unique_seen and the win counters
# - record_full_board updates full_boards counter

# Move 1: X
for x1 in range(9):
    board[x1] = 'X'
    if should_continue(board, 1):

        # Move 2: O
        for o1 in range(9):
            if board[o1] == ' ':
                board[o1] = 'O'
                if should_continue(board, 2):

                    # Move 3: X
                    for x2 in range(9):
                        if board[x2] == ' ':
                            board[x2] = 'X'
                            if should_continue(board, 3):

                                # Move 4: O
                                for o2 in range(9):
                                    if board[o2] == ' ':
                                        board[o2] = 'O'
                                        if should_continue(board, 4):

                                            # Move 5: X
                                            for x3 in range(9):
                                                if board[x3] == ' ':
                                                    board[x3] = 'X'
                                                    if should_continue(board, 5):

                                                        # Move 6: O
                                                        for o3 in range(9):
                                                            if board[o3] == ' ':
                                                                board[o3] = 'O'
                                                                if should_continue(board, 6):

                                                                    # Move 7: X
                                                                    for x4 in range(9):
                                                                        if board[x4] == ' ':
                                                                            board[x4] = 'X'
                                                                            if should_continue(board, 7):

                                                                                # Move 8: O
                                                                                for o4 in range(9):
                                                                                    if board[o4] == ' ':
                                                                                        board[o4] = 'O'
                                                                                        if should_continue(board, 8):

                                                                                            # Move 9: X
                                                                                            for x5 in range(9):
                                                                                                if board[x5] == ' ':
                                                                                                    board[x5] = 'X'

                                                                                                    # Full board reached (terminal)
                                                                                                    record_full_board(board)

                                                                                                    # undo move 9
                                                                                                    board[x5] = ' '

                                                                                        # undo move 8
                                                                                        board[o4] = ' '

                                                                            # undo move 7
                                                                            board[x4] = ' '

                                                                # undo move 6
                                                                board[o3] = ' '

                                                    # undo move 5
                                                    board[x3] = ' '

                                        # undo move 4
                                        board[o2] = ' '

                            # undo move 3
                            board[x2] = ' '

                # undo move 2
                board[o1] = ' '

    # undo move 1
    board[x1] = ' '


print(full_boards)
print(len(unique_seen), x_wins_on_full_board, draws_on_full_board, x_wins, o_wins, ties)

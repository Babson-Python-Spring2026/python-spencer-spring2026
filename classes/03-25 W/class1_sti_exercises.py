"""
Class 1 - Programs as Systems (STI exercises)
Computational Thinking with Python - Part II
"""

# ============================================================
# Exercise 1.1 - Freeze the video
# What information describes the system at a paused moment?
# ============================================================
# At a frozen moment you can see:
# - which performer is on screen (Bowie, Jagger, or both)
# - their position on the stage/set
# - the camera angle (close up, wide shot, etc)
# - what lyrics are being shown or sung
# - the current timestamp in the video
# - the lighting and colors on screen
# - whether theyre dancing, singing, standing still


# ============================================================
# Exercise 1.2 - What belongs in the state?
# ============================================================
# State items (observable facts at one frozen moment):
#   camera angle, current lyric, performer position, lighting,
#   current second in the song, who is on screen
#
# NOT state (interpretations, not observations):
#   viewer opinion, whether the song is good
#
# An observation is something you can point at on screen right now.
# An interpretation is a judgment or feeling about what you see.
# "Bowie is stage left" is observation. "Bowie looks cool" is interpretation.


# ============================================================
# Exercise 1.3 - Move from state to STI
# ============================================================
# Transitions (how the state changes):
#   - camera cuts to a new angle
#   - performers move around the stage
#   - new lyrics start
#   - timestamp advances
#   - lighting shifts between scenes
#
# Invariants (what stays true throughout):
#   - theres always at least one performer visible
#   - the song keeps playing (audio doesnt stop mid clip)
#   - the timestamp always increases
#   - its always the same two performers


# ============================================================
# Exercise 1.4 - Rephrase STI in your own words
# ============================================================
# State: the information that describes whats happening right now.
#   like a screenshot of the system at one point in time.
#
# Transition: anything that changes the state from one moment to the next.
#   something happens and the system looks different after.
#
# Invariant: a rule thats always true no matter what transitions happen.
#   if it ever breaks, something went wrong.


# ============================================================
# Exercise 1.5 - Match each structure to its purpose
# ============================================================
# variables    - store a single piece of info        - STATE (hold current values)
# expressions  - compute new values from existing    - TRANSITIONS (calculate changes)
# if statements - make decisions based on conditions  - INVARIANTS (enforce rules before changing state)
# loops        - repeat actions over a collection     - TRANSITIONS (apply changes across many items)
# dicts/lists  - store structured collections         - STATE (hold complex data like portfolios)
# functions    - package reusable operations          - TRANSITIONS (encapsulate state changes)


# ============================================================
# Exercise 1.6 - What new capability at each step?
# ============================================================
# Step 1 (variable): we can remember something. without this theres no state at all.
# Step 2 (expression): we can change what we remember. now state isnt just fixed.
# Step 3 (conditional): changes only happen when a condition is met. we can protect state.
# Step 4 (loop): we can repeat a transition many times without writing it out each time.
# Step 5 (dictionary): we can group related info together instead of having loose variables.
# Step 6 (function): we can reuse a transition without copy pasting it everywhere.


# ============================================================
# Exercise 1.7 - Which steps connect to state, transitions, invariants?
# ============================================================
# State: step 1 (variable), step 5 (dict) - these hold the data
# Transitions: step 2 (expression), step 4 (loop), step 6 (function) - these change data
# Invariants: step 3 (conditional) - this decides if a change should happen


# ============================================================
# Exercise 1.8 - Read the tiny system through STI
# ============================================================
# code:
#   count = 0
#   for ch in text:
#       if ch.isalpha():
#           count += 1
#
# State: count (int), ch (current character), text (the string being scanned)
# Transitions: each loop pass reads the next character. if its a letter, count goes up by 1.
# Invariant: count always equals the number of alphabetic characters seen so far in text.


# ============================================================
# Exercise 1.9 - Identify structures inside the loop
# ============================================================
# 1. variable (count) - stores running total
# 2. for loop - iterates through each character in text
# 3. method call (ch.isalpha()) - expression that checks if character is a letter
# 4. if statement - only increments count when the character is alphabetic
# 5. assignment/augmented assignment (count += 1) - the actual state change


# ============================================================
# Exercise 1.10 - Trace two passes (text = "A?")
# ============================================================
# Moment              | ch   | Is alphabetic? | count
# before loop begins  | -    | -              | 0
# after first pass    | "A"  | Yes            | 1
# after second pass   | "?"  | No             | 1


# ============================================================
# Exercise 1.11 - What exactly is the invariant?
# ============================================================
# "At the start of each pass through the loop, count equals
#  the number of alphabetic characters in the portion of text
#  that has already been examined."


# ============================================================
# Exercise 1.12 - Identify the state (portfolio)
# ============================================================
# cash             - yes stored state, its a variable we set directly
# positions        - yes stored state, dict tracking how many shares we own
# prices           - yes stored state, dict of current price per ticker
# portfolio_value  - NOT stored state, its derived by computing cash + sum of positions * prices


# ============================================================
# Exercise 1.13 - Simple Python structures in the portfolio
# ============================================================
# - int (cash = 10000)
# - dict (positions maps ticker strings to share counts)
# - dict (prices maps ticker strings to price values)
# - string keys in both dicts ("AAPL", "MSFT")
# - int values in positions, int/float values in prices


# ============================================================
# Exercise 1.14 - Stored state vs derived state
# ============================================================
# 1. Already stored before code runs: cash, positions, prices
# 2. Computed by the code: total_stock_value, portfolio_value
# 3. Storing portfolio_value directly is dangerous because if cash or positions
#    or prices change, portfolio_value would be stale/wrong unless you remember
#    to recompute it every time. better to just compute it when you need it.


# ============================================================
# Exercise 1.15 - Which design is better?
# ============================================================
# Model B is better. It only stores the source of truth (cash, positions, prices)
# and computes portfolio_value when needed. Model A stores portfolio_value which
# can get out of sync if you update cash or positions and forget to recalculate.
# Less stored state = fewer chances for bugs.


# ============================================================
# Exercise 1.16 - Why do we need the if statement?
# ============================================================
# 1. If condition is true: cash decreases by the cost, and positions for that
#    ticker increases by shares_to_buy. two state changes happen together.
# 2. The if statement protects the invariant that cash >= 0. Without it you could
#    buy shares you cant afford and end up with negative cash which shouldnt happen.


# ============================================================
# Exercise A - Music app by lyrics
# ============================================================
# 1. Store: song library (title, artist, full lyrics for each song), user search query
# 2. Python structures: list of dicts, each dict has keys "title", "artist", "lyrics".
#    search query is just a string.
# 3. Derived: the search results (filtered list of matching songs). you dont store the
#    results permanently, you compute them from the library + query each time.


# ============================================================
# Exercise B - Portfolio management system
# ============================================================
# 1. State: cash balance, positions (ticker -> shares), price history, transaction log
# 2. Structures: float for cash, dict for positions, dict of lists for price history,
#    list of dicts for transaction log
# 3. Derived: total portfolio value, gain/loss percentages, current allocation %


# ============================================================
# Exercise C - Tic-Tac-Toe
# ============================================================
# 1. Stored: the board (9 squares), whose turn it is
# 2. Derived: whether someone won, whether its a tie, how many moves have been made
# 3. A list of 9 elements works. each position holds a number (open), X marker, or O marker.
#    we used this exact setup in lab 2 with 1-9 for open, 10 for X, -10 for O.


# ============================================================
# Exercise D - Shopping cart
# ============================================================
# 1. State: items in cart (product name, quantity, price each), maybe a coupon code
# 2. Derived: subtotal, tax amount, total price, number of items
# 3. List of dicts works well. each dict has "name", "quantity", "price".
#    or a dict mapping product names to quantities if prices live elsewhere.


# ============================================================
# Exercise E - Airline seat map
# ============================================================
# 1. Stored: which seats exist (rows x columns), which are taken vs open,
#    passenger name for taken seats, seat class (economy, business, etc)
# 2. Collections: a 2D list (list of lists) for the seat grid, or a dict mapping
#    seat IDs like "12A" to passenger names (None if empty)
# 3. Derived: number of available seats, percent full, whether a specific row is full


# ============================================================
# Exercise F - Classroom attendance tracker
# ============================================================
# 1. After one class: a set or list of student names who were present, the date
# 2. Across the semester: dict mapping each date to a set of present students,
#    or dict mapping each student to a list of dates they attended
# 3. Stored: the raw attendance records (who was there each day)
#    Computed: total absences per student, attendance percentage, who has perfect attendance

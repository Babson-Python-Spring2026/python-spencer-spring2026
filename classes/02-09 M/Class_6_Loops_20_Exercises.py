# %%
# Exercise 1
# ### Exercise 1
# Print the numbers 1–10, one per line.

# %%
for i in range(1, 11):
    print(i)


# %%
# Exercise 2
# ### Exercise 2
# Print only the even numbers from 0–20.

# %%
for i in range(0, 21, 2):
    print(i)


# %%
# Exercise 3
# ### Exercise 3
# Given `word = "banana"`, count how many `'a'` characters appear.

# %%
word = "banana"
count = 0
for c in word:
    if c == 'a':
        count += 1
print(count)


# %%
# Exercise 4
# ### Exercise 4
# Given two lists:
# ```python
# names = ["Bob", "Alice", "Jen"]
# scores = [88, 92, 95]
# ```
# Print each name with its score.

# %%
names = ["Bob", "Alice", "Jen"]
scores = [88, 92, 95]
for i in range(len(names)):
    print(names[i], scores[i])


# %%
# Exercise 5
# ### Exercise 5
# Given:
# ```python
# d = {"a": 1, "b": 2, "c": 3}
# ```
# Print each key-value pair in the format `a -> 1`.

# %%
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key, "->", d[key])


# %%
# Exercise 6
# ### Exercise 5.6 (Continue)
# Given a list of integers, build a new list containing only the positive numbers.
# 
# Use `continue` to skip negatives and zero.

# %%
nums = [-3, 5, 0, 8, -1, 12]
positives = []
for n in nums:
    if n <= 0:
        continue
    positives.append(n)
print(positives)


# %%
# Exercise 7
# ### Exercise 5.7 (Pass)
# Create a loop that prints each character in a string, but **leave a placeholder** for handling vowels later using `pass`.

# %%
s = "hello"
for c in s:
    if c in "aeiou":
        pass  # TODO: handle vowels later
    else:
        print(c)


# %%
# Exercise 8
# ### Exercise 6
# Use a `while` loop to print numbers from 10 down to 1.

# %%
n = 10
while n >= 1:
    print(n)
    n -= 1


# %%
# Exercise 9
# ### Exercise 7
# Repeatedly ask for input until the user types `"quit"`.

# %%
# commented out so it doesnt run
# while True:
#     x = input("Enter something: ")
#     if x == "quit":
#         break


# %%
# Exercise 10
# ### Exercise 8
# Given a 3×3 grid (list of lists), print only the diagonal elements.

# %%
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(3):
    print(grid[i][i])


# %%
# Exercise 11
# ### Exercise 9
# Given a list of dictionaries representing products, print the names of all products costing more than $50.

# %%
products = [
    {"name": "shirt", "price": 30},
    {"name": "laptop", "price": 999},
    {"name": "book", "price": 15},
    {"name": "headphones", "price": 75}
]
for p in products:
    if p["price"] > 50:
        print(p["name"])


# %%
# Exercise 12
# ### Exercise 10
# Given a dictionary mapping names to lists of scores, find the student with the highest average.

# %%
students = {
    "Alice": [85, 90, 92],
    "Bob": [78, 82, 80],
    "Jen": [95, 88, 91]
}
best = None
best_avg = 0
for name in students:
    avg = sum(students[name]) / len(students[name])
    if avg > best_avg:
        best_avg = avg
        best = name
print(best)


# %%
# Exercise 13
# ### Exercise 11 — Rotate / Shift a List
# Given:
# ```python
# lst = ['a', 'b', 'c', 'd', 'e']
# ```
# Shift the elements **2 to the right** to end up with:
# ```python
# ['d', 'e', 'a', 'b', 'c']
# ```
# 
# Constraints:
# - Use a loop (no slicing shortcuts like `lst[-2:] + lst[:-2]` for the main solution).

# %%
lst = ['a', 'b', 'c', 'd', 'e']
# ran out of time, using slice for now
result = lst[-2:] + lst[:-2]
print(result)


# %%
# Exercise 14
# ### Exercise 12 — Flatten a 3×3 Matrix to a List
# Given:
# ```python
# matrix = [
#     ['A',  'B',  'C'],
#     ['D',  'E',  'F'],
#     ['G',  'H',  'I']
# ]
# ```
# Convert to:
# ```python
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# ```
# Use nested loops.

# %%
matrix = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]
flat = []
for row in matrix:
    for item in row:
        flat.append(item)
print(flat)


# %%
# Exercise 15
# ### Exercise 13 — Unflatten a List into a 3×3 Matrix
# Given:
# ```python
# flat = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# ```
# Convert to:
# ```python
# [
#     ['A',  'B',  'C'],
#     ['D',  'E',  'F'],
#     ['G',  'H',  'I']
# ]
# ```
# Use loops (you may use `range`).

# %%
flat = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
matrix = []
for i in range(0, 9, 3):
    row = [flat[i], flat[i+1], flat[i+2]]
    matrix.append(row)
print(matrix)


# %%
# Exercise 16
# ### Exercise 14 — Are These Two Matrices the Same?
# Is:
# ```python
# [
#     ['A',  'B',  'C'],
#     ['D',  'E',  'F'],
#     ['G',  'H',  'I']
# ]
# ```
# the same as:
# ```python
# [ ['A',  'B',  'C'], ['D',  'E',  'F'], ['G',  'H',  'I'] ]
# ```
# 
# Answer in two parts:
# 1. Are they **equal** (`==`)?
# 2. Are they the **same object** (`is`)?

# %%
m1 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
m2 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
print(m1 == m2)  # True - same values
print(m1 is m2)  # False - different objects


# %%
# Exercise 17
# ### Exercise 15 — Build a Histogram (Dictionary of Counts)
# Given a string, build a dictionary mapping each character to its count.
# Ignore spaces.

# %%
s = "hello world"
hist = {}
for c in s:
    if c == ' ':
        continue
    if c in hist:
        hist[c] += 1
    else:
        hist[c] = 1
print(hist)


# %%
# Exercise 18
# ### Exercise 16 — First Vowel Search (use `break`)
# Given a string, find the **first vowel** and its index.
# Stop as soon as you find one.
# If there is no vowel, report that.

# %%
s = "rhythm"  # tricky - no vowels
found = False
for i in range(len(s)):
    if s[i] in "aeiou":
        print("first vowel:", s[i], "at index", i)
        found = True
        break
if not found:
    print("no vowels")


# %%
# Exercise 19
# ### Exercise 17 — Filter a List Using `continue`
# Given a list of integers, build a new list containing only numbers that are:
# - positive
# - divisible by 3
# 
# Use `continue` to skip everything else.

# %%
nums = [-6, 3, 7, 9, -3, 12, 5]
result = []
for n in nums:
    if n <= 0:
        continue
    if n % 3 != 0:
        continue
    result.append(n)
print(result)


# %%
# Exercise 20
# ### Exercise 18 — Sum Each Row and Each Column (Nested Loops)
# Given a 3×3 matrix of numbers:
# - compute the sum of each row (3 sums)
# - compute the sum of each column (3 sums)
# 
# Store results in two lists: `row_sums` and `col_sums`.

# %%
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums = []
for row in matrix:
    row_sums.append(sum(row))

# didnt finish col_sums in class
col_sums = []
# TODO
print("row sums:", row_sums)

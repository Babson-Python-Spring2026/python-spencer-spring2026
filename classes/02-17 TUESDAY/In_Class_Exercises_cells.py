# %%
# # In-Class Function Exercises

# %%
def sum_n(n):
    """
    Return the sum of the integers from 1 to n inclusive.
    Assume n is a non-negative integer.
    Example:
    sum_n(5) -> 15
    sum_n(0) -> 0
    """
    pass

# %%
def factorial(n):
    """
    Return n factorial (n!).
    Assume n is a non-negative integer.
    Example:
    factorial(5) -> 120
    factorial(0) -> 1
    """
    pass

# %%
def fibonacci(n):
    """
    Return the nth term in the Fibonacci sequence.
    Assume:
    fibonacci(0) -> 0
    fibonacci(1) -> 1
    Example:
    fibonacci(6) -> 8
    Use a loop (not recursion).
    """
    pass

# %%
def flatten_3x3(matrix):
    """
    Given a 3x3 list of lists, return a flat list
    containing all 9 elements in row-major order.
    Example:
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
    -> [1,2,3,4,5,6,7,8,9]
    """
    pass

# %%
def reshape_to_square(lst):
    """
    Given a flat list whose length is n^2,
    return a list of lists representing an n x n matrix.
    Example:
    [1,2,3,4]
    -> [[1,2],[3,4]]
    You may assume the length is a perfect square.
    """
    pass

# %%
def ith_prime(i):
    """
    Return the ith prime number.
    Assume:
    ith_prime(1) -> 2
    ith_prime(2) -> 3
    ith_prime(3) -> 5
    You may write a helper function if needed.
    """
    pass

# %%
def is_prime(n):
    """
    Return True if n is prime.
    Return False otherwise.
    Assume n is a positive integer.
    Example:
    is_prime(2) -> True
    is_prime(15) -> False
    """
    pass

# %%
def largest_product_of_6(s):
    """
    Given a string of digits (length >= 6),
    return the largest product of any 6 consecutive digits.
    Example:
    "1234567" -> 5040
    Assume s contains only digits 0-9.
    """
# How to read in a multi line string with \n's (line returns)
# into one continuous string with no \n's or whitespace
# ------------------------------------------
# VERSION 1 — Raw multi-line string
# ------------------------------------------

'''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

digits_raw = '''
73167176 531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

print("RAW VERSION:")
print(digits_raw)


# ------------------------------------------
# VERSION 2 — Remove only newline characters
# ------------------------------------------

digits_no_newlines = digits_raw.replace("\n", "")

print("\nREMOVE NEWLINES VERSION:")
print(digits_no_newlines)


# ------------------------------------------
# VERSION 3 — Remove ALL whitespace (safest)
# ------------------------------------------

digits_clean = ''.join(digits_raw.split())

print("\nREMOVE ALL WHITESPACE VERSION:")
print(digits_clean)

# %%
def word_histogram(text):
    """
    Given a string of text, return a dictionary
    mapping each word to its frequency.
    Assume:
    - Words are separated by whitespace.
    - Convert words to lowercase.
    - Ignore punctuation.
    Example:
    "apple banana apple" -> {'apple': 2, 'banana': 1}
    """
    pass

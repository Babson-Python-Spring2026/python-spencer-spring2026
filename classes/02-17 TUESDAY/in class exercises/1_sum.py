def sum_n(n):
    """
    Return the sum of the integers from 1 to n inclusive.
    Assume n is a non-negative integer.
    Example:
    sum_n(5) -> 15
    sum_n(0) -> 0
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(5))  # 15
print(sum_n(0))  # 0

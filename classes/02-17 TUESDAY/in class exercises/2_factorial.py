def factorial(n):
    """
    Return n factorial (n!).
    Assume n is a non-negative integer.
    Example:
    factorial(5) -> 120
    factorial(0) -> 1
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120
print(factorial(0))  # 1
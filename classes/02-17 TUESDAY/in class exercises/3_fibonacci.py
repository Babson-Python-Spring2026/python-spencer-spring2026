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
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(6))  # 8
print(fibonacci(0))  # 0
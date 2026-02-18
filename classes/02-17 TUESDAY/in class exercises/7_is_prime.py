def is_prime(n):
    """
    Return True if n is prime.
    Return False otherwise.
    Assume n is a positive integer.
    Example:
    is_prime(2) -> True
    is_prime(15) -> False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(2))   # True
print(is_prime(15))  # False
print(is_prime(17))  # True

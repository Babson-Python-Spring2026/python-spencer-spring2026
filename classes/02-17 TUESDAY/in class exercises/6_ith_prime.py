def ith_prime(i):
    """
    Return the ith prime number.
    Assume:
    ith_prime(1) -> 2
    ith_prime(2) -> 3
    ith_prime(3) -> 5
    You may write a helper function if needed.
    """
    # uses is_prime from 7_is_prime.py
    def is_prime(n):
        if n < 2:
            return False
        for j in range(2, n):
            if n % j == 0:
                return False
        return True
    
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == i:
                return num
        num += 1

print(ith_prime(1))  # 2
print(ith_prime(5))  # 11
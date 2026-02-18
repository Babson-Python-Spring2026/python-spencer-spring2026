def reshape_to_square(lst):
    """
    Given a flat list whose length is n^2,
    return a list of lists representing an n x n matrix.
    Example:
    [1,2,3,4]
    -> [[1,2],[3,4]]
    You may assume the length is a perfect square.
    """
    import math
    n = int(math.sqrt(len(lst)))
    matrix = []
    for i in range(0, len(lst), n):
        matrix.append(lst[i:i+n])
    return matrix

print(reshape_to_square([1,2,3,4]))  # [[1,2],[3,4]]
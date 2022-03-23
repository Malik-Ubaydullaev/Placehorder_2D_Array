#import numpy as np
def create_arr_zeros_border_ones(n):
    """
    Create 2D array NxN of zeros. Array border is ones.
    Args:
        int: n
    Returns:
        list: 2D list
    """
    arr = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            arr[i][0], arr[i][-1] = 1, 1
            arr[0][j], arr[-1][j] = 1, 1
    return arr
print(create_arr_zeros_border_ones(5))
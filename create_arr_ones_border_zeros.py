#import numpy as np
def create_arr_ones_border_zeros(n):
    """
    Create 2D array NxN of ones. Array border is zeros.
    Args:
        int: n
    Returns:
        list: 2D list
    """
    arr = [[1] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            arr[i][0], arr[i][-1] = 0, 0
            arr[0][j], arr[-1][j] = 0, 0
    return arr
    
print(create_arr_ones_border_zeros(5))
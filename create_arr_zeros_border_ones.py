import numpy as np
def create_arr_zeros_border_ones(n):
    """
    Create 2D array NxN of zeros. Array border is ones.
    Args:
        int: n
    Returns:
        list: 2D list
    """
    arr = np.ones((n,n))
    arr[1:-1, 1:-1] = 0
    return arr

print(create_arr_zeros_border_ones(5))
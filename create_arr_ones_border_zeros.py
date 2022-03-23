import numpy as np
def create_arr_ones_border_zeros(n):
    """
    Create 2D array NxN of ones. Array border is zeros.
    Args:
        int: n
    Returns:
        list: 2D list
    """
    arr = np.zeros((n,n))
    arr[1:-1, 1:-1] = 1
    return arr
    
print(create_arr_ones_border_zeros(5))
from numpy import array


def create_arr_ones(n,m):
    """
    Create 2D array NxM of ones
    Args:
        int: n
        int: m
    Returns:
        list: 2D list
    """
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(1)
    return arr
    
    return arr
print(create_arr_ones(4,3))
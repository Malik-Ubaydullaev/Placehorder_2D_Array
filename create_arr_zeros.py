def create_arr_zeros(n,m):
    """
    Create 2D array NxM of zeros
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
            arr[i].append(0)
    return arr

print(create_arr_zeros(4,3))
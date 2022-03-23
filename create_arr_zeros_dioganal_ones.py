def create_arr_zeros_dioganal_ones(n):
    """
    Create 2D array NxN of ones. Array border is zeros.
    Args:
        int: n
    Returns:
        list: 2D list
    """
    arr = [] 
    k = 0
    for i in range(n):
        arr.append([])
        for j in range(n):
            if j == k:
                arr[i].append(1)
            else:
                arr[i].append(0)
        k += 1
    return arr
print(create_arr_zeros_dioganal_ones(5))
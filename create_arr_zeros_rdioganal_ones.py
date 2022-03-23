def create_arr_zeros_rdioganal_ones(n):
    """
    Create 2D array NxN of zeros. Array reverse dioganal is ones.
    Args:
        int: n
    Returns:
        list: 2D list
    """
    arr = [] 
    k = n
    for i in range(n):
        arr.append([])
        for j in range(n):
            if j == k - 1:
                arr[i].append(1)
            else:
                arr[i].append(0)
        k -= 1
    return arr
print(create_arr_zeros_rdioganal_ones(5))
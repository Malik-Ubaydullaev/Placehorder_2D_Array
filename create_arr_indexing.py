def create_arr_indexing(n,m):
    """
    Create 2D array Nxm of indexing.
    Args:
        int: n
        int: m
    Returns:
        list: 2D list
    """
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(m):
            arr[i].append(int(str(i+1) + str(j+1)))
    return arr
    
print(create_arr_indexing(5, 3))
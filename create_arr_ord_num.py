def create_arr_ord_num(n,m):
    """
    Create 2D array NxM
    Args:
        int: n
        int: m
    Returns:
        list: 2D list
    """
    arr = [] 
    k = 0
    for i in range(n):
        arr.append([])
        for j in range(m):
            arr[i].append(k+1)
            k += 1
    return arr
print(create_arr_ord_num(4,3))


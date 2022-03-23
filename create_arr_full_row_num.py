def create_arr_full_row_num(n,m):
    """
    Create 2D array NxM of ones
    Args:
        int: n
        int: m
    Returns:
        list: 2D list
    """
    lst = []
    
    for i in range(n):
        lst.append([])
        for j in range(m):
            lst[i].append(i)
    return lst

print(create_arr_full_row_num(4, 3))
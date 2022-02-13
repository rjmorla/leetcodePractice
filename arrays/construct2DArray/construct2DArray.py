def construct2DArray(original, m, n):
    # base case m * n invalid matrix size for original 1D array
    if m * n != len(original):
        return []
    
    # base case for when only 1 row needed in matrix
    if m == 1:
        return [original]

    res = []
    for i in range(m):
        # [i*m: i*m + n] splicing allows to split into even rows and cols to form matrix
        res.append(original[i*m: i*m + n]) # i.e. 1-4 is an splice [0:4]

    return res
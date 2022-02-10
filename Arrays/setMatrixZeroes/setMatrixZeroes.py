def setMatrixZeroes(matrix):
    #O(1)
    rows, cols = len(matrix), len(matrix[0])

    rowZero = False

    # Get which rows and cols need to be zero
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0: # if value found in matrix is 0
                matrix[0][c] = 0 # sets first row in the column to 0

                if r > 0: # prevents setting of top leftmost position to 0
                    matrix[r][0] = 0 # sets first column in that row to 0
                else:
                    rowZero = True

    # set values that aren't first row or first column to 0 if needed
    # skip first column and row to avoid setting left most column and top most row
    for r in range(1, rows): 
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix [r][0] == 0:
                matrix[r][c] = 0

    #zero out first column of matrix
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0 

    # zero out first row of matrix
    if rowZero: 
        for c in range(cols):
            matrix[0][c] = 0 
    return matrix
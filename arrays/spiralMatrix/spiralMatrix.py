# solve using a boundary system: Left, Right, Top, and Bottom Boundaries
def spiralMatrix(matrix):
    # O(m*n) speed, O(1) space
    result = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # go left to right first and get every i
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1
        
        # get every i in right most column
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        
        right -= 1

        # catch case where 1d matrices are inserted
        if not (left < right and top < bottom): 
            break
        
        # get every i in bottom row
        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        
        # shifts upwards
        bottom -= 1

        # get every i in left col
        for i in range(bottom - 1, top - 1, - 1):
            result.append(matrix[i][left])
        
        left += 1

    return result

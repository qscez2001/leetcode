'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    output = []
    m = len(matrix)
    for row in matrix:
        n = len(row)
        break

    if m == 1:
        return matrix[0]
    if n == 1:
        for i in range(m):
            output.append(matrix[i][0])
        return output

    elements = 0
    for i in range(m):
        for j in range(n):
            elements += 1

    i = 0
    j = 0
    while j < n:
        output.append(matrix[i][j])
        j += 1

    i += 1 # to next row
    j -= 1 # modify j
    while i < m:
        output.append(matrix[i][j])
        i += 1

    i -= 1
    j -= 1
    while j >= 0:
        output.append(matrix[i][j])
        j -= 1

    i -= 1
    j += 1
    while i >= 1:
        output.append(matrix[i][j])
        i -= 1

    if n > 2 and m > 2:
        sub_matrix = []
        for i in range(1, m-1):
            sub_matrix.append(matrix[i][1:n-1])
        # print(sub_matrix)
        sub_output = spiralOrder(sub_matrix)
        output = output + sub_output
    # print(output)
    return output


matrix = [[1,2,3],[4,5,6],[7,8,9]]
spiralOrder(matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiralOrder(matrix)

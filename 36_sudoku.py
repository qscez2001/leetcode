'''
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

def isValidSudoku(board):

    is_valid = True
    # each row
    for row in board:
        new_arr = []
        for ele in row:
            # print(new_arr)
            if ele == ".":
                continue
            elif ele not in new_arr:
                new_arr.append(ele)
            else:
                is_valid = False
                return is_valid

    # each column
    for i in range(0, 9):
        new_arr = []
        for column in range(0, 9):
            ele = board[column][i]
            if ele == ".":
                continue
            elif ele not in new_arr:
                new_arr.append(ele)
            else:
                is_valid = False
                return is_valid

    # 3 x 3 sub-boxes
    # (row, column)
    # (0,0)(0,3) (0,3)(3,6) (0,6)(3,9)
    # (3,0)(6,3) (3,3)(6,6) (3,6)(6,9)
    # (6,0)(9,3) (6,3)(9,6) (6,6)(9,9)
    for a in range(0, 3):
        new_arr = []
        for i in range(0, 3):
            for j in range(a*3, (a+1)*3):
                ele = board[i][j]
                if ele == ".":
                    continue
                elif ele not in new_arr:
                    new_arr.append(ele)
                else:
                    is_valid = False
                    return is_valid

    for a in range(0, 3):
        new_arr = []
        for i in range(3, 6):
            for j in range(a*3, (a+1)*3):
                ele = board[i][j]
                # print(ele)
                if ele == ".":
                    continue
                elif ele not in new_arr:
                    new_arr.append(ele)
                else:
                    is_valid = False
                    return is_valid
        # print(new_arr)

    for a in range(0, 3):
        new_arr = []
        for i in range(6, 9):
            for j in range(a*3, (a+1)*3):
                ele = board[i][j]
                if ele == ".":
                    continue
                elif ele not in new_arr:
                    new_arr.append(ele)
                else:
                    is_valid = False
                    return is_valid
        # print(new_arr)

    return is_valid




board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
print(isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
'''
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''


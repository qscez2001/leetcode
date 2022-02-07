'''
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''

# where "adjacent" cells are horizontally or vertically neighboring. 
# def dfs(word, index_i, index_j, path):


def check(word, i, j, board, path, visited):
    # print(i, j, word, path)
    # print(visited)
    if board[i][j] == word[0] and (i,j) not in visited:
        # print("en", i, j)
        visited.append((i,j))
        if not word[1:]:
            return True
    # check neighbor has next char
        if i != 0: # up exist
            up = board[i-1][j]
            # print(up, word[0])
            if word[1] == up and check(word[1:], i-1, j, board, path+up, visited):
                return True
        if i != len(board)-1: 
            down = board[i+1][j]
            if word[1] == down and check(word[1:], i+1, j, board, path+down, visited):
                return True
        if j != len(board[i])-1:
            right = board[i][j+1]
            if word[1] == right and check(word[1:], i, j+1, board, path+right, visited):
                return True
        if j != 0:
            left = board[i][j-1]
            if word[1] == left and check(word[1:], i, j-1, board, path+left, visited):
                return True   
        visited.remove((i, j))     

def exist(board, word):
    visited = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if check(word, i, j, board, "", visited):
                return True
    return False



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word))

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(exist(board, word))

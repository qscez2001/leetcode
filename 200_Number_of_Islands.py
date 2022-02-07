'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
# not solved
# dfs solution
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1
    return count

def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)

# bfs solution
# https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS
from collections import deque
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        lands=set([(i,j) for j in xrange(len(grid[0])) for i in xrange(len(grid)) if grid[i][j]=='1'])
        count=0
        while lands:
            count+=1
            i,j=lands.pop()
            connected=deque()
            connected.append((i,j))
            while connected:
                i,j=connected.popleft()
                if (i+1,j) in lands:
                    connected.append((i+1,j))
                    lands.remove((i+1,j))
                if (i-1,j) in lands:
                    connected.append((i-1,j))
                    lands.remove((i-1,j))
                if (i,j+1) in lands:
                    connected.append((i,j+1))
                    lands.remove((i,j+1))
                if (i,j-1) in lands:
                    connected.append((i,j-1))
                    lands.remove((i,j-1))
        return count
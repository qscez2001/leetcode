'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
'''
# time limit exceed
def uniquePaths(m, n):
    res = []
    solve(m, n, res)
    return sum(res)

def solve(m, n, res):
    # print(m,n)
    if m == 1 or n == 1:
        res.append(1)
    else:
        # try right
        solve(m-1, n, res)
        # try down
        solve(m, n-1, res)

# Others solution using dictionary as cache
def uniquePaths(self, m, n, cache = dict()):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if (m,n) in cache:
        return cache[(m,n)]
    
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0
    
    cache[(m, n)] = self.uniquePaths(m - 1, n, cache) + self.uniquePaths(m, n - 1, cache)
    return cache[(m, n)]

# others solution
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        # There are two possible ways to reach this cell
        return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)


m = 3
n = 2
print(uniquePaths(m, n))
m = 3
n = 3
print(uniquePaths(m, n))
m = 3
n = 7
print(uniquePaths(m, n))



'''
Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
def subsets(nums):
    subsets = []
    dfs(nums, 0, [], subsets)
    return subsets

def dfs(nums, index, path, subsets):
    subsets.append(path)
    
    for i in range(index, len(nums)):
        dfs(nums[1:], i, path+[nums[i]], subsets)

'''
Algorithm

Power set is all possible combinations of all possible lengths, from 0 to n.

Given the definition, the problem can also be interpreted as finding the power set from a sequence.

So, this time let us loop over the length of combination, 
rather than the candidate numbers, 
and generate all combinations for a given length with the help of backtracking technique.
'''
'''
We define a backtrack function named backtrack(first, curr) which takes the index of first element to add and a current combination as arguments.

If the current combination is done, we add the combination to the final output.

Otherwise, we iterate over the indexes i from first to the length of the entire sequence n.

Add integer nums[i] into the current combination curr.

Proceed to add more integers into the combination : backtrack(i + 1, curr).

Backtrack by removing nums[i] from curr.
'''

def subsets(self, nums: List[int]) -> List[List[int]]:
    def backtrack(first = 0, curr = []):
        # if the combination is done
        if len(curr) == k:  
            output.append(curr[:])
            return
        for i in range(first, n):
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()
    
    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output
        
# nums = [0]
# print(subsets(nums))
# nums = [1,2]
# print(subsets(nums))
nums = [1,2,3]
print(subsets(nums))
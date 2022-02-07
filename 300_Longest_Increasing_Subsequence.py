'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

This problem has two important attributes that let us know it should be solved by dynamic programming. 
First, the question is asking for the maximum or minimum of something. 

Second, we have to make decisions that may depend on previously made decisions, 
which is very typical of a problem involving subsequences.

'''

'''
Algorithm

1. Initialize an array dp with length nums.length and all elements equal to 1. 
dp[i] represents the length of the longest increasing subsequence that ends with the element at index i.

2. Iterate from i = 1 to i = nums.length - 1. 
At each iteration, use a second for loop to iterate from j = 0 to j = i - 1 (all the elements before i). 
For each element before i, check if that element is smaller than nums[i]. 
If so, set dp[i] = max(dp[i], dp[j] + 1).

3. Return the max value from dp.
'''

# not solved
def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)


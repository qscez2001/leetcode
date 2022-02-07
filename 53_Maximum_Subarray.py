'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle. 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647
'''
# time limit exceed
def maxSubArray(nums):

    max_sum = -2147483647

    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        sub_arr = []
        sub_arr.append(nums[i])
        sumed = sum(sub_arr)
        if sumed > max_sum:
            max_sum = sumed

        for j in range(i+1, len(nums)):
            sub_arr.append(nums[j])
            sumed = sum(sub_arr)
            if sumed > max_sum:
                max_sum = sumed

    # print(max_sum)
    return max_sum

# At each index, keep track of the maximum sum using DP table , till that point
# Save the maximum between [cur_value, max_so_far+cur_value]
# Finally, return the maximum out of the table
def maxSubArray(nums):
    dp = [0]*len(nums)
    for i,num in enumerate(nums):     
        # print("i={}, num={}".format(i, num))
        # print("dp[i-1]= ", dp[i-1])       
        dp[i] = max(dp[i-1] + num, num)
    #     print("dp[i]= ",dp[i])
    # print(dp)
    return max(dp)

# no DP
def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0: 
            nums[i] += nums[i - 1]
    #     print(nums)
    # print(nums)
    return max(nums)

# no DP too
def maxSubArray(nums):
    sums = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        sums = max(sums + nums[i], nums[i])
        max_sum = max(max_sum, sums)
    # print(max_sum)
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)
# nums = [1]
# maxSubArray(nums)
# nums = [-2147483647]
# maxSubArray(nums)
# nums = [-2,-1]
# maxSubArray(nums)
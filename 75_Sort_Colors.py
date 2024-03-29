'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
'''
def sortColors(nums):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

# others solution
# Just count how many 0, 1 and 2 we have in one pass, then replace elements accordingly.
def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    ct_0, ct_1, ct_2 = 0, 0, 0
    for i in nums:
        if i == 0:
            ct_0 += 1
        elif i == 1:
            ct_1 += 1
        elif i == 2:
            ct_2 += 1
    nums[:] = [0]*ct_0 + [1] * ct_1 + [2] * ct_2

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
nums = [0]
sortColors(nums)
print(nums)


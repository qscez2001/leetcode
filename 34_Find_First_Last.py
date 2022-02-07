'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''
def binary_search(arr, low, high, x): 
  
    mid = (high + low) // 2

    # If element is present at the middle itself 
    if arr[mid] == x: 
        return mid 

    # If element is smaller than mid, then it can only 
    # be present in left subarray 
    elif arr[mid] > x: 
        return binary_search(arr, low, mid - 1, x) 

    # Else the element can only be present in right subarray 
    else: 
        return binary_search(arr, mid + 1, high, x) 


def searchRange(nums, target: int):

    if target not in nums:
        return [-1, -1]
    else:

        if len(nums) == 1:
            return [0, 0]

        high = len(nums) - 1
        low = 0
        center = (binary_search(nums, low, high, target))
        # print(center)
        c1 = center
        while nums[c1] == target:
            if c1 == low:
                first = c1
                break
            else:
                first = c1
                c1 = c1 - 1

        c2 = center
        while nums[c2] == target:
            if c2 == high:
                last = high
                break
            else:
                last = c2
                c2 = c2 + 1

        if "last" not in locals():
            last = center
        if "first" not in locals():
            first = center
        return [first, last]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))

nums = [2, 2]
target = 2
print(searchRange(nums, target)) 

'''
nums = [5,7,7,8,8,10]
target = 6
searchRange(nums, target)

nums = []
target = 0
searchRange(nums, target)
'''

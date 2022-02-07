'''
You are given an integer array nums sorted in ascending order, 
and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand 
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''

def search(nums, target: int):

    if target not in nums:
        return -1
    else:
        return nums.index(target)
        
# Try Binery Search
def search(nums, target: int) -> int:
        
    start = 0
    end = len(nums) - 1

    while ( start <= end ):
        mid = ( start + end ) // 2
        # found the element
        if nums[mid] == target:
            return mid
        # Couldn't find the element in the list
        elif( start == mid == end ):
            return -1
        
        # start is less than mid, list is in increasing order                
        elif ( nums[start] <= nums[mid] ):
            
            # target is greater than equal to start & smaller than mid
            if( nums[start] <= target < nums[mid] ):
                end = mid
            
            # target is smaller than start & mid
            # target is greater than start & greater than mid
            else:
                start = mid + 1
        
        # start is greater than mid, list is pivoted
        else: #( nums[start] > nums[mid] ):
            # target is smaller than start & greater than mid
            if ( nums[mid] < target < nums[start] ):
                start = mid + 1
            
            # target is smaller than start & smaller than mid
            # target is greater than start & greater than mid
            else:
                end = mid

    return -1
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target))
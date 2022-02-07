'''
Given an array nums and a value val, 
remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed.

Given nums = [3,2,2,3], val = 3
return length = 2, with the first two elements of nums being 2.

Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums 
containing 0, 1, 3, 0, and 4.

'''

def lenth(nums):
    return len(nums)

def removeElement(nums, val: int):

    lenth_of_nums = len(nums)
    # i = 0
    # while i <= lenth_of_nums:
    while val in nums:
        nums.remove(val)
        lenth_of_nums = lenth(nums)
        # i += 1
    return len(nums)


# nums = [3,2,2,3]
# removeElement(nums, 3)
nums_b = [0,1,2,2,3,0,4,2]
removeElement(nums_b, 2)
def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    

    min_v = nums[len(nums)-1]
    
    rotated = [nums[len(nums)-1]] + nums[:len(nums)-1]
    # print(rotated)
    # print(min_v)
    
    while rotated[len(nums)-1] < min_v:
        min_v = rotated[len(nums)-1]  
        # print(min_v)
        rotated = [rotated[len(nums)-1]] + rotated[:len(nums)-1]
        # print(rotated)


    return min_v

# a modified version of binary search where the condition that decides the search direction would be different than in a standard binary search.
# find Inflection Point
# All the elements to the left of inflection point > first element of the array.
# All the elements to the right of inflection point < first element of the array.
'''
Algorithm

Find the mid element of the array.

If mid element > first element of array this means that we need to look for the inflection point on the right of mid.

If mid element < first element of array this that we need to look for the inflection point on the left of mid.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) / 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1

nums = [3,4,5,1,2]
print(findMin(nums))
nums = [4,5,6,7,0,1,2]
print(findMin(nums))
nums = [11,13,15,17]
print(findMin(nums))
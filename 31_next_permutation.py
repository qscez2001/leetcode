'''
Implement next permutation, which rearranges numbers into the 
lexicographically next greater permutation of numbers.

If such an arrangement is not possible, 
it must rearrange it as the lowest possible order 
(i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

[1,2,3] => [1,3,2] => [2,1,3] => [2,3,1] => [3,1,2] => [3,2,1]
'''
# not solved
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        print(nums)
    else:
        i = len(nums)-1
        while i >= 0:
            if nums[i]>nums[i-1]:
                temp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = temp
                print(nums)
                # print(nums[i])
                break
            else:
                i -= 1

# solution in leetcode. O(n)
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        print(nums)
    else:
        i = len(nums)-1
        while i > 0:
            if nums[i]>nums[i-1]:
                # find the number just large to the nums[i-1]
                score =[]
                for j in range(i, len(nums)):
                    if (nums[j] - nums[i-1]) > 0:
                        score.append(nums[j] - nums[i-1])
                    
                just_large_score = min(score)
                just_large_index = nums.index((just_large_score + nums[i-1]), i)
                # swap
                smaller = nums[i-1]
                nums[i-1] = nums[just_large_index]
                nums[just_large_index] = smaller
                # still needs to reverse i to len(nums)
                for j in range(i, len(nums)):
                    for k in range(i, len(nums)-1): # not -j
                        if nums[k] > nums[k+1]: 
                            nums[k], nums[k+1] = nums[k+1], nums[k] 
                print(nums)
                break
            else:
                i -= 1
                if i == 0:
                    nums.reverse()
                    print(nums)

# my_list = [1,2,3]
# nextPermutation(my_list)
# my_list = [3,2,1]
# nextPermutation(my_list)
# my_list = [1,1,5]
# nextPermutation(my_list)
my_list = [1,3,2]
nextPermutation(my_list)
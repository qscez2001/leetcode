'''
Given an array of non-negative integers, 
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
'''

# not solved
def canJump(nums):
    answer = False
    answer = recursive(nums)
    print(answer)
    return answer

def recursive(nums):
    last_index = len(nums) - 1
    cur = 1
    first_ele = nums[0]
    for i in range(first_ele):
        new_move = cur+i
        if new_move <= last_index:
            new_ele = nums[new_move]
            # print(new_ele)
            new_nums = nums[new_move:]
            print(new_nums)
            if len(new_nums) == 1:
                global answer
                print("in")
                answer = True
            recursive(new_nums)

    return answer
# others solution
def canJump(nums):
    m = 0
    for i, n in enumerate(nums):
        print(i, n)
        if i > m:
            return False
        m = max(m, i+n)
    return True

nums = [2,3,1,1,4]
print(canJump(nums))

nums = [3,2,1,0,4]
print(canJump(nums))
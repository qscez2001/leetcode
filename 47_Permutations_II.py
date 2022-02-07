'''
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

def another(nums, i, res):
    my_list = res
    for i in range(len(nums)-1):
        # print("j=", i)
        before = nums[0:i]
        after = nums[i+2:]
        two_num = nums[i:i+2]
        pair_nums = permuteUnique(two_num)
        new_per = before + pair_nums[1] + after
        # print(new_per)
        if new_per not in my_list:
            my_list.append(new_per)
        else: continue      
        another(new_per, 0, my_list)
    return my_list

def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 1:
        return [nums]
    elif len(nums) == 2:
        pair_list = []
        pair_list.append(nums)
        swap = []
        swap.append(nums[1])
        swap.append(nums[0])
        pair_list.append(swap)
        return pair_list
    else:
        my_list = []
        for i in range(len(nums)-1):
            # print(i)
            before = nums[0:i]
            after = nums[i+2:]
            two_num = nums[i:i+2]
            pair_nums = permuteUnique(two_num)
            new_per = before + pair_nums[1] + after
            # print(new_per)
            if new_per not in my_list:
                my_list.append(new_per)
                # permute(new_per)
            else: continue
            another(new_per, 0, my_list)

        return my_list

# modify others dfs 
def permute(nums):
    res = []
    dfs(nums, [], res)
    # remove duplicate
    new_res = []
    for item in res:
        if item not in new_res:
            new_res.append(item)
    return new_res
    
def dfs(nums, path, res):
    # print("nums=", nums)
    # print("path=", path)
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        # print(i)
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

nums = [1,1]
print(permute(nums))
# print(permuteUnique(nums))
nums = [1,1,2]
print(permute(nums))
# print(permuteUnique(nums))
nums = [1,2,3]
# print(permute(nums))
# print(permuteUnique(nums))

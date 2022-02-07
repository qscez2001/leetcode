'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

'''

# not solved
sublist = []

def combinationSum2(candidates, target, cur):
    candidates.sort()
    print(candidates)
    print("target=", target)

    if target < 0:
        return

    elif target == 0:
        current = candidates[0]
        sublist.append(cur+[current])
        print(sublist)
    else:
        current = candidates[0]
        print("cur=", current)
        combinationSum2(candidates[1:], target - current, cur+[current])

# solution...
def dfs(nums, target, index, path, res):
    # print(nums, target)
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        # print(res)
        return 
    for i in range(index, len(nums)):
        # print("index={}, i={}".format(index, i))
        if i > index and nums[i] == nums[i - 1]:
            continue
        dfs(nums, target-nums[i], i+1, path+[nums[i]], res)

def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res

# candidates = [10,1,2,7,6,1,5]
# target = 8
# print(combinationSum2(candidates, target))

candidates = [2,5,2,1,2]
target = 5
print(combinationSum2(candidates, target))
# print(sublist)
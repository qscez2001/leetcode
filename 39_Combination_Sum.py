'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
'''
'''
def candidates_to_combo(candidates, target):
    combo = []
    
    for candidate in candidates:
        N = 1
        while candidate*N < target:
            sublist = []
            for n in range(N):
                sublist.append(candidate)
            combo.append(sublist)
            N = N+1

    return combo
'''

# not solve
combo = []
def combination(candidates, target):

    if len(candidates) == 0:
        return combo
    else:
        sublist = []
        for i in range(target):
            if sum(sublist) < target:
                sublist.append(candidates[0])
                temp = sublist.copy()
                combo.append(temp)
        combination(candidates[1:], target)
        # print(combo)
        return combo


def combinationSum(candidates, target):
    # combo = candidates_to_combo(candidates, target)
    ans = []

    combo = combination(candidates, target)
    # print(combo)

    for i in range(len(combo)):
        # if any sum of two == target
        for j in range(i+1, len(combo)):
            sum_of_two = sum(combo[i] + combo[j])
            if sum_of_two == target and (combo[i] + combo[j]) not in ans:
                ans.append(combo[i] + combo[j])

    # a sum of element itself equals to target
    for item in combo:
        if sum(item) == target and item not in ans:
            ans.append(item)

    return ans

# solution
def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs(nums, target, index, path, res):
    print(index)
    print(path)
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)
    

# candidates = [2,3,6,7]
# target = 7
# print(combinationSum(candidates, target))

# candidates = [2,3,5]
# target = 8
# print(combinationSum(candidates, target))

# candidates = [2]
# target = 1
# print(combinationSum(candidates, target))
# candidates = [1]
# target = 1
# print(combinationSum(candidates, target))
# candidates = [1]
# target = 2
# print(combinationSum(candidates, target))

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))

'''
def combination(candidates, target):

    if len(candidates) == 1 and candidates[0] > target:
        return []
    elif len(candidates) == 1:
        res = []
        for i in range(target):
            res.append(candidates[0])
            if sum(res) == target:
                ans.append(res)
                return

    sublist = []
    for i in range(target):
        if sum(sublist) < target:
            sublist.append(candidates[0])
            temp = sublist.copy()
            combo.append(temp)

    # print(combo)

    for i in range(len(combo)):
        # if any sum of two == target
        for j in range(i+1, len(combo)):
            sum_of_two = sum(combo[i] + combo[j])
            if sum_of_two == target and (combo[i] + combo[j]) not in ans:
                ans.append(combo[i] + combo[j])

    # a sum of element itself equals to target
    for item in combo:
        if sum(item) == target and item not in ans:
            ans.append(item)


    if len(candidates[1:]) != 0:
        combination(candidates[1:], target)
    else:
        return
'''


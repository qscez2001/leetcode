'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''
import collections

# not passed, others solution using dictionary
def groupAnagrams(strs):
    dic = collections.defaultdict(list)
    for st in strs:
        s = ''.join(sorted(st))
        dic[s].append(st)

    return dic.values()

'''
# modify nums to chars
def permute(nums):
    res = []
    dfs(nums, "", res)
    # remove duplicate
    new_res = []
    for item in res:
        if item not in new_res:
            new_res.append(item)
    return new_res
    
def dfs(nums, path, res):

    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        # print(i)
        dfs(nums[:i]+nums[i+1:], path+nums[i], res)

def groupAnagrams(strs):
    res = []

    for i in range(len(strs)):

        flag = 0
        if res:
            for l in res:
                if strs[i] in l:
                    flag = 1
        if flag == 1:
            continue

        ele_list = []
        if strs[i]:
            all_permute = permute(strs[i])
            for item in all_permute:
                if item in strs:
                    ele_list.append(item)

            if ele_list not in res:
                res.append(ele_list)
        else:
            res.append("")

    return res

# print(permute("eat"))
'''

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# strs = [""]
# print(groupAnagrams(strs))
# strs = ["a"]
# print(groupAnagrams(strs))
# strs = ["",""]
# print(groupAnagrams(strs))

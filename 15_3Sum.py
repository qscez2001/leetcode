
# Time Limit Exceeded
def threeSum(nums):
    from itertools import combinations 
    list_of_list = []
    comb = combinations(nums, 3) 
    for i in list(comb): 
        list_of_list.append(list(i))

    ans = []
    for item in list_of_list:
        value = 0
        for num in item:
            value = value + num
        if value == 0:
            ans.append(item)

    new = []
    for item in ans:
        item.sort()
        if item not in new:
            new.append(item)

    return new

# others solution O(n^2)
# ref https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0,0,0]
nums = [-2,0,1,1,2]
print(threeSum(nums))

'''
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
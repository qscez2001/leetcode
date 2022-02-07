# fail to some testcase
def fourSum(nums, target):
    if len(nums) < 4:
        return []
    res = []
    nums.sort()
    # print(nums)

    for i in range(len(nums)-2):
        l = i+1
        r = len(nums)-1
        m = l + 1
        while l < r:
            s = nums[i] + nums[l] + nums[m] + nums[r]
            # print(nums[i], nums[l], nums[m], nums[r])
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[m], nums[r]])
                # while l < r and nums[l] == nums[l+1]:
                #     l += 1
                # while l < r and nums[r] == nums[r-1]:
                #     r -= 1
                r -= 1
                l += 1
        l = i+1
        r = len(nums)-1
        m = l + 1
        s = 0
        while m < r and m > l:
            s = nums[i] + nums[l] + nums[m] + nums[r]
            if s < target:
                m += 1
            elif s > target:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[m], nums[r]])
                # while l < r and nums[l] == nums[l+1]:
                #     l += 1
                # while l < r and nums[r] == nums[r-1]:
                #     r -= 1
                r -= 1
                m += 1
    # print(res)

    new = []
    for item in res:
        item.sort()
        if item not in new:
            new.append(item)
    
    # print(new)
    return new

# Time limit exceed
def fourSum(nums, target):
    from itertools import combinations 
    list_of_list = []
    comb = combinations(nums, 4) 
    for i in list(comb): 
        list_of_list.append(list(i))

    ans = []
    for item in list_of_list:
        value = 0
        for num in item:
            value = value + num
        if value == target:
            ans.append(item)

    new = []
    for item in ans:
        item.sort()
        if item not in new:
            new.append(item)

    return new
# others solution
# two 2Sum:
    

def fourSum(self, num, target):
"""
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    d = dict()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum2 = nums[i]+nums[j]
            if sum2 in d:
                d[sum2].append((i,j))
            else:
                d[sum2] = [(i,j)]
    
    result = set()
    for key in d:
        value = target - key
        if value in d:
            list1 = d[key]
            list2 = d[value]
            for (i,j) in list1:
                for (k,l) in list2:
                    if i!=k and i!=l and j!=k and j!=l:
                        flist = [nums[i],nums[j],nums[k],nums[l]]
                        flist.sort()
                        result.add(tuple(flist))
    return list(result)


# k-sum: Time Complexity: O(n^k−1), or O(n^3) for 4Sum.
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                    res.append([nums[i]] + set)
        return res

    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        res = []
        lo, hi = 0, len(nums) - 1
        while (lo < hi):
            sum = nums[lo] + nums[hi]
            if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return res

    nums.sort()
    return kSum(nums, target, 4)

# hash set
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return []
        if k == 2:
            return twoSum(nums, target)
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                    res.append([nums[i]] + set)
        return res

    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        res = []
        s = set()
        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res

    nums.sort()
    return kSum(nums, target, 4)

nums = [1, 0, -1, 0, -2, 2]
target = 0

print(fourSum(nums, target))

'''
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''
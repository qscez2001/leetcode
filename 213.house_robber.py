def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) < 2:
        return nums[0]
    
    numsExcludeLast = nums[:len(nums) - 1]
    numsExcludeFirst = nums[1:]
    
    excludeLastAns = robDP(numsExcludeLast)
    excludeFirstAns = robDP(numsExcludeFirst)
    
    return max(excludeLastAns, excludeFirstAns)

def robDP(nums):
    if not nums:
        return 0
    if len(nums) < 2:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print(dp)

    return max(dp)

nums = [2,3,2]
print(rob(nums))
nums = [1,2,3,1]
print(rob(nums))
nums = [1,2,3]
print(rob(nums))
# Time limit exceed
def subarraySum(self, nums: List[int], k: int) -> int:
    # find all continuous subarray
    subs = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # print(i,j)
            subarr = nums[i:j+1]
            # print(subarr)
            if sum(subarr) == k:
                subs.append(subarr)

    return len(subs)
            
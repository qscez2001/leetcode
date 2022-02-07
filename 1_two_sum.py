

# Brute Force: my solution
def twoSum(nums, target):
    for i in range(len(nums)):
        print("i=", i)
        for j in range(i+1, len(nums)):
            print("j=", j)
            if nums[i]+nums[j] == target:
                return [i, j]

# One-pass Hash Table
def twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]

# two pass hash
def twoSum(self, nums: List[int], target: int) -> List[int]:
    mylist = {}
    for i, val in enumerate(nums):
        mylist[val] = i
    # print(mylist)

    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in mylist:
            index = mylist[remain]
            if index != i:
                return [i, index]

print(twoSum([3,2,4], 6))


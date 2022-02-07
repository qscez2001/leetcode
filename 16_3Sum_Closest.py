
# Time Limit Exceeded
def threeSumClosest(nums, target):
    from itertools import combinations 
    list_of_list = []
    comb = combinations(nums, 3) 
    for i in list(comb): 
        list_of_list.append(list(i))

    # print(list_of_list)

    diff = []
    sum_of_list = []
    for item in list_of_list:
        diff.append(abs(sum(item) - target))
        sum_of_list.append(sum(item))

    index = diff.index(min(diff))
    ans = sum_of_list[index]

    return ans

# ref to Problem 15 other solution and modify O(n^2)
def threeSumClosest(nums, target):
    list_of_list = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < target:
                list_of_list.append([nums[i], nums[l], nums[r]])
                l +=1 
            elif s > target:
                list_of_list.append([nums[i], nums[l], nums[r]])
                r -= 1
            else:
                list_of_list.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1

    diff = []
    sum_of_list = []
    for item in list_of_list:
        diff.append(abs(sum(item) - target))
        sum_of_list.append(sum(item))

    index = diff.index(min(diff))
    ans = sum_of_list[index]

    return ans

# others solution, faster
def threeSumClosest(num, target):
        
    num.sort()
    result = num[0] + num[1] + num[2]
    for i in range(len(num) - 2):
        j, k = i+1, len(num) - 1
        while j < k:
            sum = num[i] + num[j] + num[k]
            if sum == target:
                return sum
            
            if abs(sum - target) < abs(result - target):
                result = sum
            
            if sum < target:
                j += 1
            elif sum > target:
                k -= 1
        
    return result


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))
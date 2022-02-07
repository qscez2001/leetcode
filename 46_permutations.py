'''
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''
# finally success myself ><
def another(nums, i, res):
    my_list = res
    for i in range(len(nums)-1):
        # print("j=", i)
        before = nums[0:i]
        after = nums[i+2:]
        two_num = nums[i:i+2]
        pair_nums = permute(two_num)
        new_per = before + pair_nums[1] + after
        # print(new_per)
        if new_per not in my_list:
            my_list.append(new_per)
        else: continue      
        another(new_per, 0, my_list)
    return my_list

def permute(nums):
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
            pair_nums = permute(two_num)
            new_per = before + pair_nums[1] + after
            # print(new_per)
            if new_per not in my_list:
                my_list.append(new_per)
                # permute(new_per)
            else: continue
            another(new_per, 0, my_list)

        return my_list

# others solution using dfs
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


# Python function to print permutations of a given list
def permutation(lst):

	# If lst is empty then there are no permutations
	if len(lst) == 0:
		return []

	# If there is only one element in lst then, only
	# one permutation is possible
	if len(lst) == 1:
		return [lst]

	# Find the permutations for lst if there are
	# more than 1 characters

	l = [] # empty list that will store current permutation

	# Iterate the input(lst) and calculate the permutation
	for i in range(len(lst)):
	m = lst[i]

	# Extract lst[i] or m from the list. remLst is
	# remaining list
	remLst = lst[:i] + lst[i+1:]

	# Generating all permutations where m is first
	# element
	for p in permutation(remLst):
		l.append([m] + p)
	return l

'''
Here is a backtrack function which takes the index of the first integer to consider as an argument backtrack(first).

If the first integer to consider has index n that means that the current permutation is done.
Iterate over the integers from index first to index n - 1.
Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
Now backtrack, i.e. swap(nums[first], nums[i]) back.
'''

def permute(self, nums: List[int]) -> List[List[int]]:
        
    def backtrack(first = 0):
        # if all integers are used up
        if first == n:
            output.append(nums[:])
        
        for i in range(first, n):
            # place i-th integer first in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # print("i={}, first={}".format(i,first))
            # print(nums)
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
            # print("a", nums)
            
    
    n = len(nums)
    output = []
    backtrack()
    
    return output

# Driver program to test above function
data = list('123')
for p in permutation(data):
	print (p)


nums = [5,4,6,2]
print(permute(nums))
# nums = [1,2,3]
# print(permute(nums))
# nums = [0,1]
# print(permute(nums))
# nums = [1]
# print(permute(nums))
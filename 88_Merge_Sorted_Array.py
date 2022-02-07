'''
Given two sorted integer arrays nums1 and nums2, 
merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) 
to hold additional elements from nums2.

:rtype: None Do not return anything, modify nums1 in-place instead.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
# not solved
def merge(nums1, m, nums2, n):
    if n == 0:
        return
    if m == 0:
        nums1 = nums2.copy()
        return
    else:
        j = 0
        for i in range(n, len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        # print(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if nums1[i] < nums1[j]:
                    temp = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = temp

def merge(nums1, m, nums2, n):
    writeIndex = m + n - 1
    m, n = m-1, n-1
    # print(writeIndex, n, m)
    while n>=0 and m>=0:
        # print(writeIndex, n, m)
        if nums1[m] > nums2[n]:
            nums1[writeIndex] = nums1[m]
            #nums1[m] = float("-inf")           We don't need to change this value because m will be pointing to m-1
            m -= 1
        else:
            nums1[writeIndex] = nums2[n]
            n -= 1
        writeIndex -= 1   
    if n > -1:
        nums1[0:n+1] = nums2[0:n+1]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1] 
m = 1
nums2 = [] 
n = 0
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)
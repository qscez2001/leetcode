
# O(logN)
def peakIndexInMountainArray(self, arr: List[int]) -> int:
    mid = len(arr) // 2
    return self.recursive(arr, mid)

def recursive(self, nums, i):
    mid = i
    if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        return  mid

    elif nums[mid] < nums[mid+1]:
        return self.recursive(nums, mid+1)
    else:
        return self.recursive(nums, mid-1)

# for loop

def peakIndexInMountainArray(self, A):
    lo, hi = 0, len(A) - 1
    while lo < hi:
        mi = (lo + hi) / 2
        if A[mi] < A[mi + 1]:
            lo = mi + 1
        else:
            hi = mi
    return lo
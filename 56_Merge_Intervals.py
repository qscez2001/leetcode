'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return 
an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
# not solved
def overlap(list_a, list_b):
    list_a_starti = list_a[0]
    list_a_endi = list_a[1]

    list_b_starti = list_b[0]
    list_b_endi = list_b[1]

    maxed = max(list_a_endi, list_b_endi)
    mined = min(list_a_starti, list_b_starti)

    if list_b_starti <= list_a_endi:
        return [mined, maxed]

# print(overlap([1,3],[4,5]))

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    if len(intervals) == 1:
        return intervals

    intervals.sort()
    res = []
    # if overlap => give a new list
    for i in range(1, len(intervals)):
        if overlap(intervals[i-1], intervals[i]):
            res.append(overlap(intervals[i-1], intervals[i]))
            continue
        else:
            if i == 1:
                res.append(intervals[i-1])
            res.append(intervals[i])
    '''
    # print(res)
    if len(res) > 1:
        while overlap(res[0], res[1]):
            if len(res) > 2:
                res = [overlap(res[0], res[1])] + res[2:]
            else: 
                res = [overlap(res[0], res[1])]
            if len(res) == 1:   break

    # print(res)
    '''
    return res
    
# jims code
def leetcode56(intervals):
    results = []

    intervals.sort()
    
    merged = None
    for i in range(len(intervals)):
        if i+1 < len(intervals):
            if merged:
                x = merged
            else:
                x =  intervals[i]

            merged = overlap(x, intervals[i+1])

            if not merged:
               results.append(x) 
        else:
            if merged:
                results.append(merged)
            else:
                results.append(intervals[i])
    
    return results

# others solution
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0: #1
        return []
    
    intervals = sorted(intervals, key = lambda x: x[0]) #2
    res = [intervals[0]] #3
    
    for current in intervals[1:]: #4
        if current[0] <= res[-1][1]: #5
            res[-1][1] = max(current[1], res[-1][1]) #6
        else: 
            res.append(current) #7
    return res #1

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# merge(intervals)
# intervals = [[1,4],[0,2],[3,5]]
# merge(intervals)
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(leetcode56(intervals))

# Approach 2: Sorting
'''
Intuition

If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

Algorithm

First, we sort the list as described. Then, we insert the first interval into our merged list 
and continue considering each interval in turn as follows: 
If the current interval begins after the previous interval ends, 
then they do not overlap and we can append the current interval to merged. 
Otherwise, they do overlap, and we merge them by updating the end of the previous interval 
if it is less than the end of the current interval.

A simple proof by contradiction shows that this algorithm always produces the correct answer. 
First, suppose that the algorithm at some point fails to merge two intervals that should be merged. 
This would imply that there exists some triple of indices ii, jj, and kk in a list of intervals \text{ints}ints such that i < j < ki<j<k and (\text{ints[i]}ints[i], \text{ints[k]}ints[k]) can be merged, but neither (\text{ints[i]}ints[i], \text{ints[j]}ints[j]) nor (\text{ints[j]}ints[j], \text{ints[k]}ints[k]) can be merged. From this scenario follow several inequalities:

ints[i].end<ints[j].start
ints[j].end<ints[k].start
ints[i].end≥ints[k].start

We can chain these inequalities (along with the following inequality, implied by the well-formedness of the intervals:

ints[i].end < ints[j].start ≤ ints[j].end < ints[k].start
                              ints[i].end ≥ ints[k].start

Therefore, all mergeable intervals must occur in a contiguous run of the sorted list.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
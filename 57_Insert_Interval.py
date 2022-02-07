'''
Given a set of non-overlapping intervals, 
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially 
sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''
# check problem 56
def insert(intervals, newInterval):
    res = []
    if len(intervals) == 0:
        res.append(newInterval)
        return res
    else:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        res.append(intervals[0])
        # print(res)
        for current in intervals[1:]:
            if current[0] <= res[-1][1]:
                res[-1][1] = max(current[1], res[-1][1])
                # print(res)
            else:
                res.append(current)
    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [2,3]
print(insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [2,7]
print(insert(intervals, newInterval))


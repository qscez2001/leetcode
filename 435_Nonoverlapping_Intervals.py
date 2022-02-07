'''
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

A classic greedy case: interval scheduling problem.

The heuristic is: always pick the interval with the earliest end time. 
Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. 
If we choose another interval with end time y, then available time slot would be [y:]. 
Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

Therefore, we can sort interval by ending time and key track of current earliest end time. 
Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.
'''

def eraseOverlapIntervals(intervals):
	end, cnt = float('-inf'), 0
	for s, e in sorted(intervals, key=lambda x: x[1]):
		if s >= end: 
			end = e
		else: 
			cnt += 1
	return cnt
'''
Solution 1: sort by starting time
Logic:

Attend the one with smaller start time first
(Greedy) Remove the one with bigger end time if overlapping occurs 
(because it will always incur more overlappings in the remaining array with asceding order of start time)

Example:

[[1,10], [2,3], [3,4], [5,6]]
First, we attend [1,10]
Next, [2,3] overlaps with [1,10] as 3 < 10. Here, we are going to remove [1,10] 
as it would definitely produce more overlappings as we continue the iteration.
Thirdly, attend [3,4]
Last, attend [5,6]

'''
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    prev = float("-inf")
    ans = 0
    for i in intervals:
        if i[0] >= prev:
            prev = i[1]
        else:
            ans += 1
            prev = min(prev, i[1])
    return ans

# my solution
def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort()
    
    count = 0
    new_intervals = []
    for inteval in intervals:
        # remove duplicated
        if inteval not in new_intervals:
            new_intervals.append(inteval)
        else:
            count += 1
    print(new_intervals)
    
    newnew_intervals = []
        
    for i in range(len(new_intervals)-2):
        # if overlap: remove the longer one
        print(new_intervals[i])
        if new_intervals[i][1] > new_intervals[i+1][0]:
            leng_a = new_intervals[i][1] - new_intervals[i][0]
            leng_b = new_intervals[i+1][1] - new_intervals[i+1][0]
            if leng_a >= leng_b:
                new_intervals.pop(i)
                # keep the shorter one
                newnew_intervals.append(new_intervals[i+1])
                count += 1
            else:
                # new_intervals.pop(i+1)
                newnew_intervals.append(new_intervals[i])
                count += 1
        else:
            newnew_intervals.append(new_intervals[i])        
    
    # print(newnew_intervals)
    return count

# similar solutions
def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals = sorted(intervals, key=lambda x:x.start)
    if len(intervals) < 2:
        return 0
    end_point = intervals[0].end
    remove = 0
    for i in range(1,len(intervals)):
        if end_point > intervals[i].start:
            remove += 1
            end_point = min(intervals[i].end,end_point)
        else:
            end_point = intervals[i].end
    return remove
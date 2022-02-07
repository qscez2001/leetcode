'''
This group would essentially go from one room to another and check if any meeting room is free.
If they find a room that is indeed free, they would start their meeting in that room. 
Otherwise, they would wait for a room to be free. 
As soon as the room frees up, they would occupy it.

We need to be able to find out efficiently if a room is available or not 
for the current meeting and 
assign a new room only if none of the assigned rooms is currently free.
'''

'''
A naive way to check if a room is available or not is to iterate on all the rooms and 
see if one is available when we have a new meeting at hand.

However, we can do better than this by making use of Priority Queues
 or the Min-Heap data structure.

Instead of manually iterating on every room that's been allocated and 
checking if the room is available or not, 
we can keep all the rooms in a min heap where the key for the min heap 
would be the ending time of meeting.

So, every time we want to check if any room is free or not, 
simply check the topmost element of the min heap as that would be the room that 
would get free the earliest out of all the other rooms currently occupied.

If the room we extracted from the top of the min heap isn't free, then no other room is. 
So, we can save time here and simply allocate a new room.

Let us look at the algorithm before moving onto the implementation.
'''
'''
Algorithm

1. Sort the given meetings by their start time.
2. Initialize a new min-heap and add the first meeting's ending time to the heap. 
    We simply need to keep track of the ending times as that tells us when a meeting room will get free.
3. For every meeting room check if the minimum element of the heap 
    i.e. the room at the top of the heap is free or not.
4. If the room is free, then we extract the topmost element and 
    add it back with the ending time of the current meeting we are processing.
5. If not, then we allocate a new room and add it to the heap.
6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. 
    This will be the minimum number of rooms needed to accommodate all the meetings.

'''
# O(NlogN).
import heapq
def minMeetingRooms(intervals):
    intervals.sort()
    heap = []
    heapq.heappush(heap, intervals[0][1])
    # print(heap)
    for i in range(len(intervals)):
        if i != 0:
            print(min(heap))
            if intervals[i][0] >= min(heap):
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
    # print(heap)
    return len(heap)

# ref: https://www.youtube.com/watch?v=FdzJmTCVyJU
# O(nlogn)
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    
    s = 0
    e = 0
    
    res = 0
    count = 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        
        res = max(res, count)
    
    return res
        
            
        

intervals = [[0,30],[5,10],[15,20]]
intervals = [[1,10],[2,7],[3,19],[11,30],[10,20],[8,12]]
minMeetingRooms(intervals)



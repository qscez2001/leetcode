'''
You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    '''
    Use the any() function. 
    This returns True if any list within the list is not empty.

    alist = [[],[]]
    if not any(alist):
        print("Empty list!")
    '''
    if not lists or not any(lists):
        return
    # add to a new array
    mylist = []
    for i in range(len(lists)):
        head = lists[i]
        while head != None:
            mylist.append(head.val)
            head = head.next

    mylist.sort()

    # make a linked list
    for i in range(len(mylist)):
        if i == 0:
            new_head = ListNode(mylist[i])
            cur = new_head
        else:
            cur.next = ListNode(mylist[i])
            cur = cur.next
    return new_head

lists = [[1,4,5],[1,3,4],[2,6]]
my_list = []
for i in lists:
    for j in range(len(i)):
        if j == 0:
            head = ListNode(i[j])
            my_list.append(head)
        else:
            head.next = ListNode(i[j])
            head = head.next

# print(my_list[0].val)
# print(my_list[0].next.val)
# print(my_list[0].next.next.val)
# print(my_list[0].next.next.next.val)
mergeKLists(my_list)

ans = [[]]
if len(ans[0]) == 0:
    print("y")
        
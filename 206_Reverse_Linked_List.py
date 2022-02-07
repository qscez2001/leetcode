'''
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode):
    if not head:
        return 
    
    stack = []
    while head != None:
        stack.append(head.val)
        head = head.next
    
    newhead = ListNode(stack.pop())
    head = newhead
    while stack:
        newhead.next = ListNode(stack.pop())
        newhead = newhead.next
    
    return head

# standard solution
def reverseList(head):
    prev = None
    curr = head
    while (curr != None):
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    return prev;

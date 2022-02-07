class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

''''
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

def removeNthFromEnd(head, n):
    current = head
    lenth = 0
    while current is not None:
        current = current.next
        lenth += 1

    # print(lenth)

    target = lenth - n + 1

    current = head
    count = 0
    prev = None
    while count < target - 1:
        prev = current
        current = current.next
        count += 1

    if target == 1:
        current = head
        head = head.next
        current = None
        return head

    prev.next = current.next
    current.next = None
    current = None
    

    # a = head
    # while a is not None:
    #     print(a.val)
    #     a = a.next

    return head

# one pass solution with dummy head
def removeNthFromEnd(self, head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in xrange(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

# Two pass algorithm
'''
Algorithm

First we will add an auxiliary "dummy" node, which points to the list head. 
The "dummy" node is used to simplify some corner cases such as a list with only one node, 
or removing the head of the list. 
On the first pass, we find the list length LL. 
Then we set a pointer to the dummy node and start to move it through the list till it comes to the (L - n)th node. 
We relink next pointer of the (L - n) th node to the (L - n + 2)=th node and we are done.
'''
def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    
    length = 0
    cur = head
    while cur is not None:
        length += 1
        cur = cur.next
    # print(length)
    
    length -= n
    cur = dummy
    while length > 0:
        length -= 1
        cur = cur.next
    # print(cur.val)
    cur.next = cur.next.next
    return dummy.next
            
        
        

head = ListNode(1)
e1 = ListNode(2)
head.next = e1
e2 = ListNode(3)
e1.next = e2
e3 = ListNode(4)
e2.next = e3
e4 = ListNode(5)
e3.next = e4


removeNthFromEnd(head, 2)

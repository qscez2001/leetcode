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

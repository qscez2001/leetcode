class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):

    array = []

    while l1:
        array.append(l1.val)
        l1 = l1.next
        
    while l2:
        array.append(l2.val)
        l2 = l2.next

    if not array:
        return None

    array.sort()

    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        node = ListNode(array[i])
        current.next = node
        current = current.next

    return head
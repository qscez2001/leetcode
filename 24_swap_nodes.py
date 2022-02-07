# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes.
# Only nodes itself may be changed.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
# don't use while :(
def swapPairs(head: ListNode) -> ListNode:
    current = head
    count = 0
    while current != None:
        if current.next is not None:
            temp = current.next
            temp1 = current     
            temp1.next = temp.next
            current = temp
            current.next = temp1
            
            if count == 0:
                new_head = current
            
            count += 2
            current = current.next.next
        # else:
        #     current = current.next
        #     count += 1
        # print(current.val)
    return new_head
'''

def dump(my_list: ListNode):
    print("===============")
    current = my_list
    while current != None:
        print(current.val)
        current = current.next

# jim's code
def swapPairs(head: ListNode) -> ListNode:
    if head == None:
        return head
    elif head.next == None:
        return head
    else:
        x = head
        y = head.next
        z = head.next.next

        head = y
        head.next = x        
        head.next.next = swapPairs(z)

        return head

    


head = [1,2,3,4]

my_list = ListNode(head[0])
current = my_list
for i in range(1, len(head)):
    node = ListNode(head[i])
    current.next = node
    current = current.next

dump(my_list)

my_list = swapPairs(my_list)

dump(my_list)


# head = []
# head = [1]
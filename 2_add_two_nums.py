# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(2)
e2 = ListNode(4)
e3 = ListNode(3)
l1.next = e2
e2.next = e3

l2 = ListNode(5)
a2 = ListNode(6)
a3 = ListNode(4)
l2.next = a2
a2.next = a3

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def addTwoNumbers(l1, l2):
    str1 = ''
    str2 = ''
    while l1:
        str1 = str1 + str(l1.val)
        l1 = l1.next

    while l2:
        str2 = str2 + str(l2.val)
        l2 = l2.next

    new_s1 = ''
    new_s2 = ''
    for i in str1: 
        new_s1 = i + new_s1

    for i in str2: 
        new_s2 = i + new_s2
    
    num1 = int(new_s1)
    num2 = int(new_s2)
    num = num1 + num2

    ans = ''
    for i in str(num): 
        ans = i + ans
    # print(ans)

    l3 = ListNode(ans[0])
    current = l3
    for i in range(1, len(ans)):
        current.next = ListNode(ans[i])
        current = current.next

    return l3

print(addTwoNumbers(l1,l2))

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

        
# Approach 1: Recursion
'''
Algorithm

1. Since we are given a linked list and not an array, we don't really have access to the elements of the list using indexes. 
We want to know the middle element of the linked list.

2. We can use the two pointer approach for finding out the middle element of a linked list. 
Essentially, we have two pointers called slow_ptr and fast_ptr. 
The slow_ptr moves one node at a time whereas the fast_ptr moves two nodes at a time. 
By the time the fast_ptr reaches the end of the linked list, the slow_ptr would have reached the middle element of the linked list. 
For an even sized list, any of the two middle elements can act as the root of the BST.

3. Once we have the middle element of the linked list, we disconnect the portion of the list to the left of the middle element. 
The way we do this is by keeping a prev_ptr as well which points to one node before the slow_ptr i.e. prev_ptr.next = slow_ptr. 
For disconnecting the left portion we simply do prev_ptr.next = None

4. We only need to pass the head of the linked list to the function that converts it to a height balances BST. 
So, we recurse on the left half of the linked list by passing the original head of the list and 
on the right half by passing slow_ptr.next as the head.
'''

def sortedListToBST(self, head):
    prev = None
    slow = fast = head
    
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        prev = slow
    
    prev.next = None
    
    root = Node(slow.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(slow.next)
    
# Approach 2: Recursion + Conversion to Array
'''
Algorithm

1. Convert the given linked list into an array. Let's call the beginning and the end of the array as left and right
2. Find the middle element as (left + right) / 2. Let's call this element as mid. 
    This is a O(1) time operation and is the only major improvement over the previous algorithm.
3. The middle element forms the root of the BST.
4. Recursively form binary search trees on the two halves of the array represented by (left, mid - 1) and (mid + 1, right) respectively.
'''
def sortedListToBST(self, head):
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return helper(0, len(arr)-1, arr)
        
def helper(self, l, r, arr):
    # Invalid case
    if l > r:
        return None

    # Middle element forms the root.
    mid = (l + r) // 2
    node = TreeNode(arr[mid])

    # Base case for when there is only one element left in the array
    if l == r:
        return node

    # Recursively form BST on the two halves
    node.left = self.helper(l, mid - 1, arr)
    node.right = self.helper(mid + 1, r, arr)
    return node

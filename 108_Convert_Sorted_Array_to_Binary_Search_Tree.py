'''
Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as 
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    if not root:
        return []
    my_list = []
    q = deque()
    q.append(root)

    while q:
        # print(q)
        # for i in q:
        #     print(i.val)
        new_level = []
        for i in range(len(q)):
            u = q.popleft()
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
            new_level.append(u.val)
        my_list.append(new_level)

    return my_list

def sortedArrayToBST(nums):
    if not nums:
        return
    length = len(nums)
    middle = length // 2
    # print(nums)
    root = TreeNode(nums[middle])
    # print(root.val)
    root.left = sortedArrayToBST(nums[0:middle])
    root.right = sortedArrayToBST(nums[middle+1:])
    return root

nums = [-10,-3,0,5,9]
root = sortedArrayToBST(nums)
print(levelOrder(root))



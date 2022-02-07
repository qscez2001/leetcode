'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# not solved correctly BFS
# https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/272253/python-very-easy-to-understand-queue-solution
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

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
    
# bt = [3,9,20,null,null,15,7]
s = TreeNode(val=7, left=None, right=None)
fi = TreeNode(val=15, left=None, right=None)
n = TreeNode(val=9, left=None, right=None)
t = TreeNode(val=20, left=fi, right=s)
root = TreeNode(val=3, left=n, right=t)
print(levelOrder(root))
'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode):
    depth = []
    if not root:
        return 0

    recursive(root, 0, depth)
    # print(depth)
    return max(depth)

def recursive(root, dep, depth):
    dep += 1
    # print(dep)
    depth.append(dep)
    if root.left:
        recursive(root.left, dep, depth)
    if root.right:
        recursive(root.right, dep, depth)

    return dep

# root = [3,9,20,null,null,15,7]
s = TreeNode(val=7, left=None, right=None)
fi = TreeNode(val=15, left=None, right=None)
n = TreeNode(val=9, left=None, right=None)
t = TreeNode(val=20, left=fi, right=s)
root = TreeNode(val=3, left=n, right=t)
print(maxDepth(root))
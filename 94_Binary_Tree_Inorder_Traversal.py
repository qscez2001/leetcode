'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):

    res = []

    traverse(root, res)

    return res



def traverse(root: TreeNode, res):
    if root == None:
        return
    else:
        if root.left:
            # print(root.val)
            traverse(root.left, res)

        res.append(root.val)

        if root.right:
            traverse(root.right, res)
    

root = [1,None,2,3]

three = TreeNode(val=3, left=None, right=None)
two = TreeNode(val=2, left=three, right=None)
root = TreeNode(val=1, left=None, right=two)

print(inorderTraversal(root))
root = []
root = [1]
root = [1,2]
root = [1,None,2]



'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# not solved

'''
A simple solution would be to use the in-order tree traversal. 
Read this first before moving forward. Once you know how this example work, 
we can use it for this problem. 
What we do is to first get the in-order traverse in an array! 
Since the input is a binary tree, 
each element in the in-order travelsal result (res) should be less than the one after it. 
We get res, then we go over every element of res and check wether each element is less than the one after it. 
If it's not the case, we return False. Otherwise, True.


'''
def isValidBST(root: TreeNode):
    res = []
    traverse(root, res)

    for i in range(len(res)-1):
        if res[i] >= res[i+1]:
            return False
    return True

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



root = [2,1,3]
one = TreeNode(val=1, left=None, right=None)
three = TreeNode(val=3, left=None, right=None)
root = TreeNode(val=2, left=one, right=three)
print(isValidBST(root))


# root = [5,1,4,null,null,3,6]
one = TreeNode(val=1, left=None, right=None)
three = TreeNode(val=3, left=None, right=None)
six =TreeNode(val=6, left=None, right=None)
four = TreeNode(val=4, left=three, right=six)
root = TreeNode(val=5, left=one, right=four)
print(isValidBST(root))
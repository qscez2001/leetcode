'''
Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
# not solved
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode):
    if root == None:
        return True
    return valid(root.left, root.right)

def valid(left, right):
    # if left.val == right.val:
    if left and right:
        return left.val == right.val and valid(left.left, right.right) and valid(left.right, right.left)
    else:
        return left == right


    
# [1,2,2,2,null,2]
two4 = TreeNode(val=2, left=None, right=None)
two3 = TreeNode(val=2, left=None, right=None)
two = TreeNode(val=2, left=two3, right=None)
two2 = TreeNode(val=2, left=two4, right=None)
root = TreeNode(val=1, left=two, right=two2)
print(isSymmetric(root))


three = TreeNode(val=3, left=None, right=None)
three2 = TreeNode(val=3, left=None, right=None)
two = TreeNode(val=2, left=None, right=three)
two2 = TreeNode(val=2, left=None, right=three2)
root = TreeNode(val=1, left=two, right=two2)
print(isSymmetric(root))

# [1,2,2,3,4,4,3]
four = TreeNode(val=4, left=None, right=None)
four4 = TreeNode(val=4, left=None, right=None)
three = TreeNode(val=3, left=None, right=None)
three2 = TreeNode(val=3, left=None, right=None)
two = TreeNode(val=2, left=three, right=four)
two2 = TreeNode(val=2, left=four4, right=three2)
root = TreeNode(val=1, left=two, right=two2)
print(isSymmetric(root))

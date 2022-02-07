'''
Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.
Two binary trees are considered the same if they are 
structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

# not entirly solved
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right) 
            # isSameTree(p.left, q.left)
            # isSameTree(p.right, q.right)
    else:
        return p == q
# simpler
def isSameTree(self, p, q): 
    # p and q are both None
    if not p and not q:
        return True
    # one of p and q is None
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.right, q.right) and \
           self.isSameTree(p.left, q.left)
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# not entirely solve
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/34115/Python-easy-to-understand-deque-solution
def zigzagLevelOrder(root: TreeNode):
    if not root:
        return []
    my_list = []
    q = deque()
    q.append(root)
    count = 0

    while q:
        count += 1
        # print("level= ", count)
        # print(q)
        # for i in q:
        #     print(i.val)
        new_level = []
        # if count % 2 == 0:
        #     q.reverse()
        for i in range(len(q)):
            u = q.popleft()
            new_level.append(u.val)
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
        # print(new_level)
        if count % 2 == 0:
            new_level = new_level[::-1]
        my_list.append(new_level)

    return my_list


# bt = [3,9,20,null,null,15,7]
f = TreeNode(val=4, left=None, right=None)
fi = TreeNode(val=5, left=None, right=None)
th = TreeNode(val=3, left=None, right=fi)
t = TreeNode(val=2, left=f, right=None)
root = TreeNode(val=1, left=t, right=th)
print(zigzagLevelOrder(root))

s = TreeNode(val=7, left=None, right=None)
fi = TreeNode(val=15, left=None, right=None)
n = TreeNode(val=9, left=None, right=None)
t = TreeNode(val=20, left=fi, right=s)
root = TreeNode(val=3, left=n, right=t)
print(zigzagLevelOrder(root))
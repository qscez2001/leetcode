'''
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. 
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space 
does not count as extra space for this problem.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
your function should populate each next pointer to point to its next right node, just like in Figure B. 
The serialized output is in level order as connected by the next pointers, 
with '#' signifying the end of each level.
'''

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def recursive(root, i):
    num_nodes = pow(2, i)
    print("-------")
    print("num_nodes= ", num_nodes)
    print("-------")
    print(root)
    if not root:
        return
    head = Node(root[0])
    for j in range(num_nodes):
        print(head.val)
        print(j)
        head.next = Node(root[j])
        head = head.next

    i += 1
    recursive(root[num_nodes:], i)
# not solved
def connect(root):
    i = 0
    recursive(root, i)

# others solutions
def connect(self, root):
    """
    :type root: TreeLinkNode
    :rtype: nothing
    """
    
    if not root:
        return None
    cur  = root
    next = root.left

    while cur.left :
        cur.left.next = cur.right
        if cur.next:
            cur.right.next = cur.next.left
            cur = cur.next
        else:
            cur = next
            next = cur.left

    return root

# dfs
def connect(self, root: 'Node') -> 'Node':
    """
      1 (1)
    2 (2)->  3(1)
 4(4) -> 5(3) -> 6(2) -> 7(1)
    """
    self.dfs(root)
    return root

## (1). left child -> right child
## (2). right child -> next.left child
def dfs(self,root):
    if root == None or root.left == None:
        return
    root.left.next = root.right
    if root.next != None: 
        root.right.next = root.next.left
    self.dfs(root.left)
    self.dfs(root.right)


root = [1,2,3,4,5,6,7]
connect(root)


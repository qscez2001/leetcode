'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# the first preorder is head
# inorder is used for split the left and right


def buildTree(self, preorder: List[int], inorder: List[int]):
    if not inorder or not preorder:
        return None
    head = preorder[0]
    index = inorder.index(head)
    root = TreeNode(head)

    root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
    root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
    return root

# not entirely solved
def find_the_first(preorder, inorder):
    # print(preorder, inorder)
    if not inorder or not preorder:
        return None
    head = preorder[0]
    index = inorder.index(head)
    root = TreeNode(head)

    root.left = find_the_first(preorder[1:index+1], inorder[0:index])
    root.right = find_the_first(preorder[index+1:], inorder[index+1:])
    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(find_the_first(preorder, inorder).val)
# https://zhenyu0519.github.io/2020/03/11/lc105/#code


'''
Algorithm

Build a hashmap to record the relation of value -> index for inorder, 
so that we can find the position of root in constant time.

Initialize an integer variable preorderIndex to keep track of the element 
that will be used to construct the root.

Implement the recursion function arrayToTree which takes a range of inorder and 
returns the constructed binary tree:
if the range is empty, return null;
initialize the root with preorder[preorderIndex] and then increment preorderIndex;
recursively use the left and right portions of inorder to construct the left and right subtrees.
Simply call the recursion function with the entire range of inorder.
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)
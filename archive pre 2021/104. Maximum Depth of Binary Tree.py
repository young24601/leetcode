"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is not None:
            if root.right is not None:
                return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
            else:
                return self.maxDepth(root.left)+1
        else:
            if root.right is not None:
                return self.maxDepth(root.right)+1
            else:
                return 1


s = Solution()
tree3 = TreeNode(3)
tree9 = TreeNode(9)
tree20 = TreeNode(20)
tree15 = TreeNode(15)
tree7 = TreeNode(7)
tree3.left = tree9
tree3.right = tree20
tree20.left = tree15
tree20.right = tree7
assert 3 == s.maxDepth(tree3)

treeA1 = TreeNode(1)
treeA2 = TreeNode(2)
treeA3 = TreeNode(3)
treeA1.left = treeA2
treeA2.left = treeA3
assert 3 == s.maxDepth(treeA1)

treeB1 = TreeNode(1)
treeB2 = TreeNode(2)
treeB3 = TreeNode(3)
treeB1.right = treeB2
treeB2.right = treeB3
assert 3 == s.maxDepth(treeB1)

tree = None
assert 0 == s.maxDepth(tree)

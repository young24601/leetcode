"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


s = Solution()
tree4 = TreeNode(4)
tree2 = TreeNode(2)
tree7 = TreeNode(7)
tree4.left = tree2
tree4.right = tree7
tree1 = TreeNode(1)
tree3 = TreeNode(3)
tree6 = TreeNode(6)
tree9 = TreeNode(9)
tree2.left = tree1
tree2.right = tree3
tree7.left = tree6
tree7.right = tree9

tree = s.invertTree(tree4)

print(tree)

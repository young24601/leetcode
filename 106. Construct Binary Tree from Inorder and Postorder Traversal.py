# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
#####################################

# recall that 
# inorder is circling around with numbers from the bottom (Left, Root, Right)
# postorder is circling around with numbers coming from the right (Left, Right, Root)

# preorder is circling around with numbers coming from the left (Root, Left, Right)
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        
        
        
test = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
test.buildTree(inorder, postorder)


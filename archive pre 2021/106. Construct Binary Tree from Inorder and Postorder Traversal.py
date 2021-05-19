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
        # last item of postorder is the root.  you can break up the inorder by postorder to get the left/right sides
        
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        root = TreeNode(postorder.pop())
 
        #get the index of the root value
        i = inorder.index(root.val)
        #break up left side using the index
        leftSideInorder = inorder[0:i]
        leftSidePostorder = postorder[0:i]
        #and right side using the index.  note you need the +1 for inorder to ignore the root value but in postorder it's already gone
        rightSideInorder = inorder[inorder.index(root.val)+1:]
        rightSidePostorder = postorder[i:]
        #recurse left/right 
        root.left = self.buildTree(leftSideInorder, leftSidePostorder)
        root.right = self.buildTree(rightSideInorder, rightSidePostorder)
        return root

        
import queue        
def bfs(root):
    L = queue.Queue()
    
    while root != None:
        print(root.val,end=',')
        if root.left != None:
            L.put(root.left)
        if root.right != None:
            L.put(root.right)
        
        if L.empty():
            return
        else:
            root = L.get()
        
test = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
result = test.buildTree(inorder, postorder)
bfs(result)

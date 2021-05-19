#105. Construct Binary Tree from Preorder and Inorder Traversal
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #first element of preorder gives us the root.
        #get the index of the root in the inorder array and use that to split the preorder array left/right
        
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        #pop preorder at index 0 which gives us the root value
        root = TreeNode(preorder.pop(0))
        #set i = index of the root in the inorder array
        i = inorder.index(root.val)
        print(root.val, i)
        print(preorder,inorder)
        root.left = self.buildTree(preorder[:i], inorder[:i])
        root.right = self.buildTree(preorder[i:], inorder[i+1:])
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
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
t = s.buildTree(preorder, inorder)
bfs(t)


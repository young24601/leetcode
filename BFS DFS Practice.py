import queue

class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


def dfs(root):
    print(root.data,end=',')
    if root.left != None:
        dfs(root.left)
    if root.right != None:
        dfs(root.right)

def bfs(root):
    L = queue.Queue()
    
    while root != None:
        print(root.data,end=',')
        if root.left != None:
            L.put(root.left)
        if root.right != None:
            L.put(root.right)
        
        if L.empty():
            return
        else:
            root = L.get()
            
    
if __name__ == "__main__":
    nodeF = Node("F")
    nodeD = Node("D")
    nodeJ = Node("J")
    nodeB = Node("B")
    nodeE = Node("E")
    nodeG = Node("G")
    nodeK = Node("K")
    nodeA = Node("A")
    nodeC = Node("C")
    nodeI = Node("I")
    nodeH = Node("H")
    
    nodeF.left = nodeD
    nodeF.right = nodeJ
    nodeD.left = nodeB
    nodeD.right = nodeE
    nodeJ.left = nodeG
    nodeJ.right = nodeK
    nodeB.left = nodeA
    nodeB.right = nodeC
    nodeG.right = nodeI
    nodeI.left = nodeH

    dfs(nodeF)
    print()
    bfs(nodeF)
    
# Return the total sum of all leaf nodes in a n-ary tree in O(1) Space. You cannot use recursion as the call stack uses memory.
# You can construct the node class as you choose.
# You cannot use any extra space, the solution has to be in O(1) space

class Node():
    def __init__(self, val, children = []):
        self.val = val
        self.next = None
        self.children = children
    def __repr__(self):
        return str(self.val)


def sum_of_leaves(root):
    if len(root.children) == 0:
        return root.val
    sum = 0

    while root:
        print("at node " + str(root.val))
        next = root.children[0]
        ct = 0
        while root:
            print("ct: " + str(ct) + "(" + str(root.children[ct].val) + "," + str(root.children[ct+1].val) + ")")
            if len(root.children[ct].children) == 0:
                sum += root.val
            root.children[ct].next = root.children[ct+1]
            root.children[ct+1].next = root.next and root.next.children[0]
            root = root.next
            ct += 1
        root = next
    return 0

n8 = Node(8)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, [n4, n5])
n3 = Node(3, [n7])
n1 = Node(1, [n2, n3, n8])

assert 24 == sum_of_leaves(n1)

#24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
#
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        start_node = curr = ListNode(0)
        start_node.next = head
        while curr.next != None and curr.next.next != None:
            n1, n2 = curr.next, curr.next.next
            print(curr,n1,n2)
            curr.next = n2
            n1.next = n2.next
            n2.next = n1
            curr = curr.next.next
        return start_node.next

s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
e = None

sol = s.swapPairs(e)
print("printing solution:")
while sol != None:
    print(sol.val, end=',')
    sol = sol.next

#25. Reverse Nodes in k-Group

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    """ListNode doc string"""
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        start_node = temp_node = ListNode(0)
        start_node.next = group_head = group_tail = head

        while True:
            ct = 0
            # go to the next node of the tail until we reach the end or we reach k
            while group_tail != None and ct < k:
                group_tail = group_tail.next
                ct += 1

            if ct == k:
                # if we reached k, then we know that group_tail is pointing at the node after k nodes
                # We should reverse each node between group_head and before group_tail and then connect the new
                # group head to the group_tail
                left, right = group_head, group_tail

                for _ in range(0, k):
                    # flip each node and make the left's next node the group_tail (for the first iteration)
                    # and then subsequently initial left node that was just completed
                    left.next, left, right  = right, left.next, left

                # now we need to connect the previous group with this one
                # set the temp_node (initial node) to left (which is the node after k nodes), temp_node.next to
                # the right node (which is the k-th element of the cycle), and left to
                temp_node.next, temp_node, group_head = right, group_head, group_tail

            else:
                return start_node.next

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

sol = s.reverseKGroup(a, 1)
print("printing solution:")
while sol != None:
    print(sol.val, end=',')
    sol = sol.next

# sol = s.reverseKGroup(a, 3)
# print("printing solution:")
# while sol != None:
#     print(sol.val, end=',')
#     sol = sol.next

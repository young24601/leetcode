#21. Merge Two Sorted Lists

#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if (l1 == None): return l2
        if (l2 == None): return l1

        if (l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


s = Solution()

c = ListNode(4)
b = ListNode(2)
b.next = c
a = ListNode(1)
a.next = b

cc = ListNode(4)
bb = ListNode(3)
bb.next = cc
aa = ListNode(1)
aa.next = bb

l1 = a
l2 = aa


l1 = c
l2 = cc

zzz = s.mergeTwoLists(l1, l2)





print("*******")
while True:
    if zzz != None:
        print(zzz.val, sep=",")
        zzz = zzz.next
    if zzz == None:
        break

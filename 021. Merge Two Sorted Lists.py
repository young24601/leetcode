# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        ret = ""
        while self.next != None:
            ret += str(self.val) + " -> "
            self = self.next
        ret += str(self.val)
        return str(ret)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if (l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



        # ct1, ct2 = 0, 0
        # l = []
        # this is for regular lists...
        # while ct1 < len(l1) or ct2 < len(l2):
        #     if ct1 == len(l1):
        #         l.extend(l2[ct2:])
        #         return(l)
        #     elif ct2 == len(l2):
        #         l.extend(l1[ct1:])
        #         return(l)
        #     elif l1[ct1] < l2[ct2]:
        #         l.append(l1[ct1])
        #         ct1 += 1
        #     else:
        #         l.append(l2[ct2])
        #         ct2 += 1
        # return(l)


s = Solution()

a1 = ListNode(1)
a11 = ListNode(3)
a111 = ListNode(5)
a1.next = a11
a11.next = a111
a2 = ListNode(2)
a22 = ListNode(4)
a222 = ListNode(6)
a2222 = ListNode(8)
a2.next = a22
a22.next = a222
a222.next = a2222
a3 = ListNode(1)
a33 = ListNode(2)
a333 = ListNode(3)
a3333 = ListNode(4)
a33333 = ListNode(5)
a333333 = ListNode(6)
a3333333 = ListNode(8)
a3.next = a33
a33.next = a333
a333.next = a3333
a3333.next = a33333
a33333.next = a333333
a333333.next = a3333333

assert a3 == s.mergeTwoLists(a1, a2)

# assert [1,2,3,4,5,6,8] == s.mergeTwoLists([1,3,5], [2,4,6,8])
# assert [1,1,2,3,4,4] == s.mergeTwoLists([1,2,4], [1,3,4])
# assert [0] == s.mergeTwoLists([], [0])
# assert [0] == s.mergeTwoLists([0], [])
# assert [1,2,3] == s.mergeTwoLists([1,2,3], [])
# assert [] == s.mergeTwoLists([], [])
# assert [-3,-2,-1,-1,0,2,3,4,4] == s.mergeTwoLists([-3,-1,2,4], [-2,-1,0,3,4])

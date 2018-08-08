#19. Remove Nth Node From End of List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # have two pointers, one which is traversing the list and one that is n nodes ahead
        # this way, when the one ahead comes to the end, the first node skips the next node
        back = head
        front = head
        for _ in range(0,n):
            front = front.next
        if front == None:
            return head.next
        while front.next != None:
            back = back.next
            front = front.next
        if back.next != None:
            back.next = back.next.next
        return head


e = ListNode(5)
d = ListNode(4)
d.next = e
c = ListNode(3)
c.next = d
b = ListNode(2)
b.next = c
a = ListNode(1)
a.next = b

s = Solution()
#zzz = s.removeNthFromEnd(a, 2)

aa = ListNode(1)
zzz = s.removeNthFromEnd(aa, 1)
print(zzz)
while True:
    if zzz != None:
        print(zzz.val, sep=",")
        zzz = zzz.next
    if zzz == None:
        break

#23. Merge k Sorted Lists

#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)
    # def __lt__(self, other):
    #         return self.val < other.val

import bisect


import heapq
class Solution:
    # put the head of every linked list into a heap.  Then pop the smallest value and add it to the solution list
    # and then add the next node to the heap
    def mergeKLists(self, lists):
        head = current_node = ListNode(0)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            #val, n = heap[0]
            node = heapq.heappop(heap)
            index = node[1]
            current_node.next = node[2]
            current_node = current_node.next
            if current_node.next:
                heapq.heappush(heap, (current_node.next.val, index, current_node.next))
        return head.next

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

    #simply merge two lists k-1 times...  too slow
    def mergeKListsTooSlow(self, lists):
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        l = lists[0]
        for ct in range(1, len(lists)):
            l = self.mergeTwoLists(l, lists[ct])

        return l


    # leetcode doesn't accept this as I cannot add the __lt__ to ListNode..
    def mergeKListsNotAccepted(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sorted_list = None
        head = None
        current_nodes = []

        for ct in range(0, len(lists)):
            if lists[ct] != None:
                bisect.insort(current_nodes, lists[ct])

        while current_nodes != []:
            p = current_nodes.pop(0)
            if sorted_list == None:
                sorted_list = p
                head = sorted_list
            else:
                sorted_list.next = p
                sorted_list = sorted_list.next
            if p.next != None:
                bisect.insort(current_nodes, p.next)
        return head





a = ListNode(1)
aa = ListNode(4)
aaa = ListNode(5)
a.next = aa
aa.next = aaa


b = ListNode(1)
bb = ListNode(3)
bbb = ListNode(4)
b.next = bb
bb.next = bbb

c = ListNode(2)
cc = ListNode(6)
c.next = cc

s = Solution()
sol = s.mergeKLists([a,b,c])

print("printing solution:")
while sol != None:
    print(sol.val, end=',')
    sol = sol.next

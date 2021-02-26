# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        myString = ""
        while self is not None:
            myString += str(self.val)
            if self.next is not None:
                myString += " -> "
            self = self.next
        return myString

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        sumRoot = None
        sum = sumRoot
        currentSum = 0
        carryOne = False
        while (carryOne) or (l1) or (l2):
            #print(l1, "and", l2, "carry", carryOne)
            if carryOne:
                currentSum = 1
            else:
                currentSum = 0
            carryOne = False

            if l1:
                currentSum += l1.val
                l1 = l1.next
            if l2:
                currentSum += l2.val
                l2 = l2.next

            if currentSum >= 10:
                carryOne = True

            #print(f"Added {currentSum % 10}")
            if sum:
                #print("Old")
                sum.next = ListNode(currentSum % 10)
                sum = sum.next
            else:
                #print("New")
                sum = ListNode(currentSum % 10)
                sumRoot = sum

            #print("sum",sum)
            #print("sumRoot", sumRoot)
        #print(sumRoot)
        return sumRoot


s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
ans = ListNode(7)
ans.next = ListNode(0)
ans.next.next = ListNode(8)
ans == s.addTwoNumbers(l1, l2)
l1 = ListNode(0)
l2 = ListNode(0)
ans = ListNode(0)
ans == s.addTwoNumbers(l1, l2)
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
ans = ListNode(8)
ans.next = ListNode(9)
ans.next.next = ListNode(9)
ans.next.next.next = ListNode(9)
ans.next.next.next.next = ListNode(0)
ans.next.next.next.next.next = ListNode(0)
ans.next.next.next.next.next.next = ListNode(0)
ans.next.next.next.next.next.next.next = ListNode(1)
ans == s.addTwoNumbers(l1, l2)

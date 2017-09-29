# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        current = self
        myString = ""
        while True:
            myString += str(current.val)
            if current.next != None:
                myString += " -> "
                current = current.next
            else:
                break
        return myString
        
    

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        listSolution = None
        current = listSolution
        carry = 0
        while True:
            if l1 != None:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2 != None:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            print("Adding " + str(v1) + " + " + str(v2) + " (" + str(carry) + ")")
            sumNode = ListNode((v1 + v2 + carry) % 10)
            
            if (v1 + v2 + carry) >= 10:
                carry = 1
            else:
                carry = 0
            
            if listSolution == None:
                listSolution = sumNode
                current = sumNode
            else:
                current.next = sumNode
                current = current.next

            
            if (l1 == None and l2 == None and carry == 0):
                break
        return listSolution
            
            
                

        
        
        
list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)
list2 = ListNode(5)        
list2.next = ListNode(6)
list2.next.next = ListNode(4)
list3 = ListNode(2)
list3.next = ListNode(1)
list4 = ListNode(9)
                        

test = Solution()
#print(test.addTwoNumbers(list1, list2))
#print(test.addTwoNumbers(list1, list3))
#print(test.addTwoNumbers(list3, list4))
print(test.addTwoNumbers(list4, list4))


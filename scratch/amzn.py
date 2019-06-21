# Given a continous stream of characters, find the first non repeating character at any given point => https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/
# Given a tree with left, right and next pointer,
# update next pointer to point to the right node at same level => https://leetcode.com/problems/populating-next-right-pointers-in-each-node/. Told the interviewer that I'd already done the question
# Given two arrays containing numbers, find the difference of closest greatest of each number from left and right ?
# 3 2 1 7 5
# 0 3 2 0 7 => from left (here for number 1 since 2 and 3 are both greater, we pick the closest viz. 2)
# 7 7 7 0 0 => from right
# 7 4 5 0 7 => difference
import queue

class Node():
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    def __repr__(self):
        return str(self.val)

def question_one():
    stream = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s", "a"]

    stream_set = set()
    stream_valid = {}

    for item in stream:
        if item not in stream_set:
            #print("New", item)
            stream_set.add(item)
            stream_valid[item] = True
        else:
            #print("Old", item)
            if item in stream_valid:
                stream_valid.pop(item)
        curr = list(stream_valid)[0]
        print("Current", curr)




def question_two(root):
    head = root
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
            root = root.next
        root = next
    return(head)

node4 = Node("4", None, None, None)
node5 = Node("5", None, None, None)
node2 = Node("2", node4, node5, None)
node6 = Node("6", None, None, None)
node7 = Node("7", None, None, None)
node3 = Node("3", node6, node7, None)
node1 = Node("1", node2, node3, None)

q2 = question_two(node1)

# Given two arrays containing numbers, find the difference of closest greatest of each number from left and right ?
# 3 2 1 7 5
# 0 3 2 0 7 => from left (here for number 1 since 2 and 3 are both greater, we pick the closest viz. 2)
# 7 7 7 0 0 => from right
# 7 4 5 0 7 => difference
def question_three():

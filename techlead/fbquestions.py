#!/usr/bin/python3
import queue


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def __repr__(self):
        return self.data


def bfs(root, root2, node):
    L = queue.Queue()
    L2 = queue.Queue()

    while root is not None:
        print("data:", root.data)
        if root.data == node.data:
            return root2

        if root.left is not None:
            L.put(root.left)
            L2.put(root2.left)
        if root.right is not None:
            L.put(root.right)
            L2.put(root2.right)

        if L.empty():
            return
        else:
            root = L.get()
            root2 = L2.get()


def question1():
    treeA = Node("1")
    treeA.left = Node("2")
    node3A = Node("3")
    node3A.left = Node("4")
    node3A.right = Node("5")
    treeA.right = node3A

    treeB = Node("1")
    treeB.left = Node("2")
    node3B = Node("3")
    node3B.left = Node("4")
    node3B.right = Node("5")
    treeB.right = node3B

    # find Node("3") on both trees
    found_node = bfs(treeA, treeB, Node("3"))
    print("found_node", found_node)


def question2():
    arr = [1, 0, 0, 2, 5, 0]

    last_index = len(arr) - 1
    for i in range(len(arr)-1, 0, -1):
        if arr[i] != 0:
            last_index = i
            break

    ct = 0
    print("initial:", arr)
    while (ct <= last_index):
        if arr[ct] == 0:
            arr[ct], arr[last_index] = arr[last_index], arr[ct]
            last_index -= 1
        ct += 1

    print("final:", arr)


def validate_parentheses(input):
    parentheses = []
    for c in input:
        print(parentheses, c)
        if c in ("(", "["):
            parentheses.append(c)
        elif c == ")":
            if parentheses.pop() != "(":
                return False
        elif c == "]":
            if parentheses.pop() != "[":
                return False
    return True


def remove_invalid_parentheses(input):
    output = []
    for c in input:
        print(parentheses, c)
        if c in ("(", "["):
            parentheses.append(c)
            output.append(c)
        elif c == ")":
            if parentheses.pop() != "(":
                return False
        elif c == "]":
            if parentheses.pop() != "[":
                return False
    return output


def question3():
    print(validate_parentheses("(([()(]))"))
    print(remove_invalid_parentheses("(([()(]))"))


class techlead_data:
    def __init__(self, size, data):
        self.size = size
        self.data = data


def question4():
    arr = [techlead_data("S", 123), techlead_data("M", 456), techlead_data("L", 789), techlead_data("S", 12), techlead_data("M", 45), techlead_data("L", 78)]
    # a = sorted(arr, key=lambda x: "SML".index(x.size))
    arr.sort(key=lambda x: "SML".index(x.size))
    for item in arr:
        print(item.size, item.data)
    return arr



question4()

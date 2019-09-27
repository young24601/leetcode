
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        print("pushed", x)
        self.stack.append(x)
        if (len(self.min_stack) == 0) or (x <= self.min_stack[-1]):
            print("pushing to minstack", x)
            self.min_stack.append(x)
        return

    def pop(self) -> None:
        if len(self.min_stack) > 0 and len(self.stack) > 0 and self.min_stack[-1] == self.stack[-1]:
            print("min pop", self.min_stack.pop())

        print("popped", self.stack.pop())
        return

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        return 0


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print("getmin..", obj.getMin())   # Returns -3.
obj.pop()
print("top..", obj.top())  # Returns 0.
print("getmin..", obj.getMin())   # Returns -2.

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

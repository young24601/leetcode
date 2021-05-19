# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Example:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

import queue

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue(size)
        self.sum = 0.0
        self.current_size = 0
        self.max_size = size

    def next(self, val: int) -> float:
        if self.current_size >= self.max_size:
            self.sum -= self.q.get()
        else:
            self.current_size += 1
        self.sum += val
        self.q.put(val)
        return self.sum / self.current_size

s = MovingAverage(3)
param_1 = s.next(1)
param_2 = s.next(10)
param_3 = s.next(3)
param_4 = s.next(5)

print(param_1) # 1
print(param_2) # 5.5
print(param_3) # 4.6666
print(param_4) # 6

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

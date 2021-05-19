"""
n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.

n digit password of digits 0 to k
find a "password" that is guaranteed to unlock the safe

n=1, k=2: 01 or 10
n=2, k=2: 00, 01, 10, 11 -> 00 01 11 10 -> 00110
n=2, k=3: 00, 01, 02, 10, 11, 12, 20, 21, 22 -> 
n=3, k=2: 000, 001, 010, 011, 100, 101, 110, 111
n=3, k=3: 000, 001, 002, 010, 011, 012, 020, 021, 022
          100, 101, 102, 110, 111, 112, 120, 121, 122
          200, 201, 202, 210, 211, 212, 220, 221, 222

"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        return

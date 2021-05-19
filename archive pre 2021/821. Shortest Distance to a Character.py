"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
from typing import List

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # try a solution with two passes, one forward and one backward...
        shortest_distances = []
        ct = 99999
        for c in list(S):
            if c == C:
                ct = 0
            else:
                ct += 1
            shortest_distances.append(ct)
        current_index = len(shortest_distances) - 1
        ct = 99999
        for c in list(S)[::-1]:
            if c == C:
                ct = 0
            else:
                ct += 1
            shortest_distances[current_index] = min(ct, shortest_distances[current_index])
            current_index -= 1

        return shortest_distances

s = Solution()

print(s.shortestToChar("asdfeasdf", 'e'))
print(s.shortestToChar("asdfasdfe", 'e'))
print(s.shortestToChar("esdfasdfg", 'e'))
print(s.shortestToChar("asdfeeasdef", 'e'))


#print(s.shortestToChar("loveleetcode", 'e'))
#assert [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0] == s.shortestToChar("loveleetcode", 'e')






class SolutionThatDidntWorkWell:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        chars = list(S)
        start = 0
        end = len(S)
        current_index = 0
        shortest_distances = []

        ct = start = S.index(C, start, end)
        while ct >= 0:
            shortest_distances.append(ct)
            ct -= 1
        start += 1

        ct = 0
        while C in S[start:end]:
            print("Checking", S[start:end], "at", start, end)
            next_index = S.index(C, start, end)
            print("found", next_index)

            print("doing1", start, "to", (start + next_index) // 2)
            for i in range(start, (start + next_index) // 2):
                shortest_distances.append(ct)
                print("doing1", shortest_distances, ct)
                ct += 1
            if start == next_index:
                print("reset index")
                ct = 0
            elif (start + next_index) % 2 == 0:
                print("elif")
                ct -= 1
            print("doing2", (start + next_index) // 2, "to", next_index)
            for i in range((start + next_index) // 2, next_index+1):
                shortest_distances.append(ct)
                ct -= 1
                print("doing2", shortest_distances, ct)
            start = next_index+1

        ct = 1
        for i in range(start, end):
            shortest_distances.append(ct)
            ct += 1
            print("end", shortest_distances)

        print(shortest_distances)
        return shortest_distances

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # zip will combine the lists by characters that are unpacked by *
        # like: [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        prefix = ""
        for l in list(zip(*strs)):
            if len(set(l)) == 1: # if len is 1 it means all chars are equal
                prefix += l[0]
            else:
                return prefix
        return prefix

s = Solution()

assert "fl" == s.longestCommonPrefix(["flower","flow","flight"])
assert "" == s.longestCommonPrefix(["dog","racecar","car"])
assert "" == s.longestCommonPrefix([""])

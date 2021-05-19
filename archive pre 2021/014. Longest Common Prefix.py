#14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# 
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # need to match each character and location and find the longest one from the start
        # taking *strs breaks down each string and places them in a tuple
        # we can go through the tuples and put them in a set 
        prefix = ""
        for l in zip(*strs):
            if len(set(l)) == 1:
                prefix += l[0]
            else:
                return prefix
        return prefix 
        
s = Solution()
assert s.longestCommonPrefix([]) == ""
assert s.longestCommonPrefix("") == ""
assert s.longestCommonPrefix([""]) == ""
assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
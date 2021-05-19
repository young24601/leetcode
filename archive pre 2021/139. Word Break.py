# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # break up each iteration of the words into pieces of all sizes

        has_path = [False] * (len(s) + 1)
        if s == "":
            return True
        else:
            has_path[0] = True # there is a path to the first element
            for i in range(1, len(s)+1): # iterate through each letter
                for j in range(0, i):
                    #print(f"Checking {s[j:i]}")
                    if has_path[j] and s[j:i] in wordDict:
                        #print(f"Setting has_path[{i}] to True")
                        has_path[i] = True
                        break
        return has_path[-1]


s = Solution()
assert True == s.wordBreak("leetcode", wordDict = ["leet", "code"])
assert True == s.wordBreak("applepenapple", wordDict = ["apple", "pen"])
assert True == s.wordBreak("applepenapple", wordDict = ["applepe", "apple", "pen"])
assert True == s.wordBreak("applepeapple", wordDict = ["applepe", "apple", "pen"])
assert True == s.wordBreak("applepenapplepeapple", wordDict = ["applepe", "apple", "pen"])
assert False == s.wordBreak("catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])

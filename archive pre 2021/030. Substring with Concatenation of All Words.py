# 030. Substring with Concatenation of All Words
# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# Example 1:
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:
#
# Input:
#   s = "wordgoodstudentgoodword",
#   words = ["word","student"]
# Output: []


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # the problem is to find each instance of concatenation of all words in the string

        return


s = Solution()
assert [0,9] == s.findSubstring("barfoothefoobarman", ["foo","bar"])

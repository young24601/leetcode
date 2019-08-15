# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence
# where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not self.wordBreakI(s, wordDict):
            return []
        # print("has path:", self.wordBreakI(s, wordDict))
        word_list = [[] for _ in range(len(s) + 1)]
        has_path = [False] * (len(s) + 1)
        if s == "":
            return True
        else:
            has_path[0] = True # there is a path to the first element
            for i in range(1, len(s)+1): # iterate through each letter
                for j in range(0, i):
                    if has_path[j] and s[j:i] in wordDict:
                        has_path[i] = True
                        # print("Checking", j, word_list[j])
                        if len(word_list[j]) > 0:
                            # print("len > 0", word_list[j], "adding", s[j:i], "to index", i, word_list[i])
                            # word_list[i].append(s[j:i])
                            for word in word_list[j]:
                                # print("adding " + word + " " + s[j:i] + " TO word_list[" + str(i) + "]")
                                word_list[i].append(word + " " + s[j:i])
                        else:
                            # print("len = 0", "adding", s[j:i], "to index", i, word_list[i])
                            word_list[i].append(s[j:i])
                        # break
        #print(word_list[len(s)])
        return word_list[len(s)]

    def wordBreakI(self, s: str, wordDict: List[str]) -> bool:
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
assert sorted(["cats and dog", "cat sand dog"]) == sorted(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
assert sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]) == sorted(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
assert sorted([]) == sorted(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

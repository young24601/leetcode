from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # one way is to sort the letters using sorted and compare them to the original list.

        new_list = sorted(words, key=lambda word: [order.index(c) for c in word])
        # for word in words:
        #     for c in word:
        #         print(c, order.index(c))
        #     print(word)
        #
        print(words)
        print(new_list)
        return words == new_list


s = Solution()

s.isAlienSorted(["abcde", "edcba"], "edcba")

assert True is s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")

assert False is s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")

assert False is s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")

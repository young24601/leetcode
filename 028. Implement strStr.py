#28. Implement strStr()

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # iterate through each letter in haystack and check for a match in needle.  if
        # there is a match, keep track of the initial index and iterate through each letter
        # in needle until the end is reached (return the index) or there is a mismatch
        # and you continue the process from index+1

        if needle == "" or needle == haystack:
            return 0
        elif len(needle) > len(haystack) or haystack == "":
            return -1

        ct = 0
        prev = 0
        while ct < len(haystack):
            if haystack[ct] == needle[ct - prev]:
                if ct-prev == len(needle)-1:
                    return prev
                ct += 1
            else:
                ct = prev + 1
                prev = ct

        if haystack[ct:] == needle:
            return ct

        return -1

s = Solution()

assert s.strStr("", "asdf") == -1
assert s.strStr("asdf", "") == 0
assert s.strStr("", "a") == -1
assert s.strStr("a", "") == 0
assert s.strStr("a", "a") == 0
assert s.strStr("asdfkjiedjwlkdjfdij", "aliejfalijflakdfjkldjsflaijeslifjkdfj") == -1

assert s.strStr("hello", "ll") == 2
assert s.strStr("aaaaa", "bba") == -1
assert s.strStr("aaaaab", "aab") == 3
assert s.strStr("aaaaa", "bba") == -1

# if needle == "" or haystack == "" or len(needle) > len(haystack):
#             if needle == "" or (needle == "" and haystack == ""):
#                 return 0
#             return -1
#
#         in_cycle = False
#         prev = 1
#         index_needle = 0
#         index_haystack = 0
#         ct = 0
#         print("Len haystack:", len(haystack))
#         while ct < len(haystack):
#             print("ct:", ct)
#             print("needle:",needle[index_needle], "vs haystack:", haystack[index_haystack])
#             if needle[index_needle] == haystack[index_haystack]:
#                 print("Match and in_cycle:", in_cycle)
#                 if not in_cycle:
#                     in_cycle = True
#                     prev = ct
#                 else:
#                     index_needle += 1
#                     index_haystack += 1
#                 if len(needle) == index_needle:
#                     return prev
#             else:
#                 print("Mismatch", prev)
#                 prev += 1
#                 if in_cycle:
#                     print("Was in cycle, resetting ct to", prev)
#                     ct = prev
#                 in_cycle = False
#
#                 index_haystack += 1
#             ct += 1
#         print("prev:", prev)
#         if in_cycle:
#             return prev
#         return -1

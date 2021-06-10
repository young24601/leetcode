# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # ideally should be one pass.  a suboptimal solution is to index
        # each time you find a match and "go back"

        if needle == "":
            return 0

        i_haystack = 0
        i_needle = 0
        found = -1
        while i_haystack < len(haystack):
            #print(f"checking {haystack[i_haystack]} (at {i_haystack}) vs {needle[i_needle]} (at {i_needle})")
            if haystack[i_haystack] == needle[i_needle]:
                #print(f"match {i_needle} with found: {found}")
                if i_needle == 0:
                    found = i_haystack
                if i_needle == len(needle) - 1:
                    #print(f"i_haystack: {i_haystack}. found: {found}")
                    return found
                i_haystack += 1
                i_needle += 1
            else:
                i_needle = 0
                if found != -1:
                    #print(f"reset back to {found}")
                    i_haystack = found + 1
                    found = -1
                else:
                    #print(f"increment")
                    i_haystack += 1
        return -1


s = Solution()
assert 2 == s.strStr("hello", "ll")
assert -1 == s.strStr("aaaaaa", "bba")
assert 0 == s.strStr("", "")
assert 0 == s.strStr("llllll", "lll")
assert 3 == s.strStr("abclllabcll", "lll")
assert 9 == s.strStr("llallallalllalll", "lll")
assert 4 == s.strStr("mississippi", "issip")
assert 3 == s.strStr("ississippi", "issip")
assert 0 == s.strStr("issippi", "issip")

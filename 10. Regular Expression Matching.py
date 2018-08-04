#10. Regular Expression Matching

class Solution:
    def isMatch(self, s, p):
        # initialize [p] * [s] array
        sol = [[False for i in range(0,len(p)+1)] for j in range(0,len(s)+1)]
        
        # Define sol[i][j] to be True if s[0 to i] matches p[0 to j]
        # This gives us three scenarios.  The simple case where we must match the next character with the same character or a . captured in the else
        # This case sets the value of sol[i][j] to be sol[i-1][j-1] and whether there is a match
        # In the event of a *, then we will either have no matches or one or more matches
        #  With 0 matches, then simply go back to sol[i][j-2], or the bool before the * expression
        #  With 1 or more matches, then see if s[i-1] is equal to the character with the * expression p[j-2] (or equal to .) and set it to 
        #   the bool that we had with the previous string value sol[i-1][j]
        sol[0][0] = True
        for i in range(0, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    sol[i][j] = sol[i][j-2] or (i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.')) and sol[i-1][j]
                else:
                    sol[i][j] = i>0 and sol[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return sol[len(s)][len(p)]
        
        
        


s = Solution()
assert s.isMatch("aa", "a") == False
assert s.isMatch("aa", "a*") == True
assert s.isMatch("ab", ".*") == True
assert s.isMatch("aab", "c*a*b") == True
assert s.isMatch("mississippi", "mis*is*p*.") == False

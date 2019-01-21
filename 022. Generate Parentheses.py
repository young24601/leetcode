#22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        return self.generate_parentheses_helper('', n, 0)

    # idea here is that whenever you are out of open parentheses (number_available == 0), close all of them
    # if the number_unclosed == 0, then you have to add a new open parenthesis and recurse with number_available-- and number_unclosed++
    # if available > 0 and unclosed > 0 then we have the choice of either adding an open parenthesis or closing it.  recurse accordingly
    # probably should keep track of all outputs according to number_available and number_unclosed to avoid recursing on conditions we know
    def generate_parentheses_helper(self, current_string, number_available, number_unclosed):
        if number_available == 0:
            return [current_string + ')' * number_unclosed]
        elif number_unclosed == 0:
            return self.generate_parentheses_helper(current_string + '(', number_available - 1, number_unclosed + 1)

        return self.generate_parentheses_helper(current_string + '(', number_available - 1,
                number_unclosed + 1) + self.generate_parentheses_helper(current_string + ')', number_available, number_unclosed - 1)



s = Solution()
print(len(s.generateParenthesis(5)))

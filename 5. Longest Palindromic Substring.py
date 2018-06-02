class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) <= 1:
            return s
        for letter in s:
            print(letter)
        
        
        


test = Solution()
print(test.longestPalindrome('babad')) #bab
#print(test.longestPalindrome('cbbd')) #bb
#print(test.longestPalindrome('asdfeasdabbaasdfeadf')) #abba
#print(test.longestPalindrome('a'))
#print(test.longestPalindrome('aa'))

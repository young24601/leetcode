#9. Palindrome Number
#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        num = x
        while num > 0:
            rev = 10 * rev + num % 10
            num = num // 10
        print(x,rev)
        return x == rev
        


s = Solution()
s.isPalindrome(121)
s.isPalindrome(-121)
s.isPalindrome(10)

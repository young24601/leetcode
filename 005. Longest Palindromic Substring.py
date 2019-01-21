"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

Input: "aaa"
Output: "aaa"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Naive way would be to go to each character and try to go left and right from it
        # for as long as it remains a palindrome.

        if len(s) <= 1:
            return s

        longestString = s[0]
        
        for ct in range(0, len(s) - 1):
            #odd case
            currentString = s[ct]
            left = ct - 1
            right = ct + 1
            while (left >= 0 and right < len(s)):
                if s[left] == s[right]:
                    currentString = s[left] + currentString + s[right]
                    if len(currentString) > len(longestString):
                        longestString = currentString
                    left -= 1
                    right += 1
                else:
                    break
            
            #even case
            if ct+1 <= len(s) and s[ct] == s[ct+1]:
                currentString = s[ct] + s[ct+1]
                left = ct - 1
                right = ct + 2
                if len(currentString) > len(longestString):
                        longestString = currentString
                while (left >= 0 and right < len(s)):
                    if s[left] == s[right]:
                        currentString = s[left] + currentString + s[right]
                        if len(currentString) > len(longestString):
                            longestString = currentString
                        left -= 1
                        right += 1
                    else:
                        break
                
            
            
        
        # There can be two types of palindromes fixing on a point n.  The letters could reflect on n
        # like 123n321 (odd length) or could include n like 123nn321 (even length).
        
        return longestString
        



        
t = Solution()

i = "aaaa" #output c, expected bb
print(t.longestPalindrome(i))
# i = "cbbd" #output c, expected bb
# print(t.longestPalindrome(i))
# i = "ccc" #output c, expected bb
# print(t.longestPalindrome(i))
# 
# i = "abqxzzxqb" #even
# print(t.longestPalindrome(i))
# i = "a" #output c, expected bb
# print(t.longestPalindrome(i))
# #sol = t.longestPalindrome(i)
# #assert sol == "a"
# i = "" #output c, expected bb
# print(t.longestPalindrome(i))
# i = "babad" #output c, expected bb
# print(t.longestPalindrome(i))
# i = "543qzcvdeqXqedvczq123" #output c, expected bb
# print(t.longestPalindrome(i))
# i = "bqxzzxqb" #output c, expected bb
# print(t.longestPalindrome(i))


#i = "543qzcvdeqXqedvczq123" #odd
#sol = t.longestPalindrome(i)
#assert sol == "qzcvdeqXqedvczq" or sol == ""


i = "abqxzzxqb" #even
#sol = t.longestPalindrome(i)
#assert sol == "bqxzzxqb" or sol == ""

#i = "babad"
#sol = t.longestPalindrome(i)
#assert sol == "bab" or sol == "aba" or sol == ""

#i = "cbbd"
#sol = t.longestPalindrome(i)
#assert sol == "bb" or sol == ""
#  
# 
#     
# def longestPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     # Naive way would be to go to each character and try to go left and right from it
#     # for as long as it remains a palindrome.
# 
#     if len(s) <= 1:
#         return s
# 
#     longestString = s[0]
#     
#     for ct in range(0, len(s) - 1):
#         #odd case
#         currentString = s[ct]
#         left = ct - 1
#         right = ct + 1
#         while (left >= 0 and right < len(s)):
#             if s[left] == s[right]:
#                 currentString = s[left] + currentString + s[right]
#                 if len(currentString) > len(longestString):
#                     longestString = currentString
#                 left -= 1
#                 right += 1
#             else:
#                 break
#         
#         #even case
#         if ct+1 <= len(s) and s[ct] == s[ct+1]:
#             currentString = s[ct] + s[ct+1]
#             left = ct - 1
#             right = ct + 2
#             if len(currentString) > len(longestString):
#                     longestString = currentString
#             while (left >= 0 and right < len(s)):
#                 if s[left] == s[right]:
#                     currentString = s[left] + currentString + s[right]
#                     if len(currentString) > len(longestString):
#                         longestString = currentString
#                     left -= 1
#                     right += 1
#                 else:
#                     break
#             
#         
#         
#     
#     # There can be two types of palindromes fixing on a point n.  The letters could reflect on n
#     # like 123n321 (odd length) or could include n like 123nn321 (even length).
#     
#     return longestString    
#     
    
    
    # if len(s) <= 1:
    #     return s
    # for letter in s:
    #     print(letter)
    # 
    #     
        
# 
# 
# test = Solution()
# print(test.longestPalindrome('babad')) #bab
# #print(test.longestPalindrome('cbbd')) #bb
# #print(test.longestPalindrome('asdfeasdabbaasdfeadf')) #abba
# #print(test.longestPalindrome('a'))
# #print(test.longestPalindrome('aa'))
# 
#         for ct in range(0, len(s) - 1):
#             
#             #do odd length case first
#             left = ct - 1
#             right = ct + 1
#             currentString = s[ct]
#             while left > 0 and right < len(s):
#                 if s[left] == s[right]:
#                     currentString = s[left] + currentString + s[right]
#                     if len(currentString) > len(longestString):
#                         longestString = currentString
#                     left -= 1
#                     right += 1
#                 else:
#                     break
#                 
#             #do even length case
#             if s[ct] == s[ct+1]:
#                 #qualifies
#                 left = ct - 1
#                 right = ct + 2
#                 currentString = s[ct] + s[ct+1]
#                 longestString = currentString
#                 while left > 0 and right < len(s):
#                     if s[left] == s[right]:
#                         currentString = s[left] + currentString + s[right]
#                         if len(currentString) > len(longestString):
#                             longestString = currentString
#                         left -= 1
#                         right += 1
#                     else:
#                         break
#         return longestString
#         

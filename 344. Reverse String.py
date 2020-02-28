# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(len(s), len(s)//2+1)
        for i in range(len(s) // 2):
            print(f"swapping {i} ({s[i]}) with {len(s) - 1 - i} ({s[len(s) - i - 1]})")
            s[i], s[len(s) - 1 - i] = s[len(s) - i - 1], s[i]
        return s

s = Solution()
assert ["o","l","l","e","h"] == s.reverseString(["h","e","l","l","o"])
assert ["h","a","n","n","a","H"] == s.reverseString(["H","a","n","n","a","h"])


assert ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"] == s.reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"])


a = ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," "," ","a",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]
b = ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]

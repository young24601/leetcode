#17. Letter Combinations of a Phone Number

#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

from functools import reduce
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {'1':None, '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
        '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '0':None, '*':None, '#':None}

        #first construct the compositions of each letter into a list
        letters = [mapping[i] for i in digits]
        if digits:
            if len(digits) == 1:
                return mapping[digits]
            else:
                return reduce(lambda x, y: [i + j for i in x for j in y], letters)
        else:
            return []







s = Solution()
print(s.letterCombinations('3'))
print(s.letterCombinations('23'))


test = [1,2,3,4,5]

#print(reduce(lambda x: [i * j for i in x for j in y], test))

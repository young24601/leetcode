# There is a special keyboard with all keys in a single row.
#
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
# initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character.
# The time taken to move your finger from index i to index j is |i - j|.
#
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
#
# Example 1:
#
# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4.
# Example 2:
#
# Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
# Output: 73
#
#
# Constraints:
#
# keyboard.length == 26
# keyboard contains each English lowercase letter exactly once in some order.
# 1 <= word.length <= 10^4
# word[i] is an English lowercase letter.

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        alphabet = {}
        index = 0
        for letter in keyboard:
            alphabet[letter] = index
            index += 1

        current_index = 0
        keyboard_sum = 0
        for letter in word:
            #print("Checking", letter)
            #print(alphabet[letter],"-", current_index)
            keyboard_sum += abs(alphabet[letter] - current_index)
            current_index = alphabet[letter]
            #print("Sum:", keyboard_sum)

        return keyboard_sum



s = Solution()
assert 4 == s.calculateTime("abcdefghijklmnopqrstuvwxyz", "cbba")
assert 11 == s.calculateTime("pqrstuvwxyzabcdefghijklmno", "a")

assert 73 == s.calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode")

#assert 1 == s.calculateTime("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

# Given an input of two strings, write a method to determine if the two strings are anagrams
# (composed of the same set of letters) of each other. Letter uppercase/lowercase state is ignored.

# Examples:
# isAnagramMatch("melon", "lemon") => true
# isAnagramMatch("ocean", "canoe") => true
# isAnagramMatch("battle", "tablet") => true
# isAnagramMatch("reserve", "reverse") => true
# isAnagramMatch("bob", "rob") => false

# The latter input string can contain wildcard characters ("*") which can represent any single letter.
# Example:
# isAnagramMatch("melon", "lemo*") => true


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    wildcards = 0
    s = list(s1)
    for letter in s2:
        if letter == '*':
            wildcards += 1
        elif letter in s1:
            # print("remove", letter, "from", s)
            s.remove(letter)
        else:
            return False

    return len(s) == wildcards


assert False is is_anagram("asdf", "asdff")
assert False is is_anagram("asdff", "asdf")
assert False is is_anagram("5", "4")
assert True is is_anagram("the word", "theword ")
# assert True is is_anagram("melon", "lemon")
# assert True is is_anagram("ocean", "canoe")
# assert True is is_anagram("battle", "tablet")
# assert True is is_anagram("reserve", "reverse")
# assert False is is_anagram("bob", "rob")
# assert True is is_anagram("melon", "l**on")


# Given an array of integers greater than zero, find if it is possible to split
# it in two subarrays, such that the sum of the two subarrays is the same. Print the two subarrays.
# You cannot reorder the initial array.
#
# Examples:
# [1,2,3,3,1,1,1] -> [1,2,3] [3,1,1,1]
# [1,5,4,3,6,1] -> [1,5,4] [3,6,1]


def split_array(a):
    if len(a) < 2:
        return False

    left = a[0]
    right = sum(a[1:])
    i = 1
    while left < right:
        if left == right:
            return True
        left += a[i]
        right -= a[i]
        i += 1

    return True


assert True is split_array([1, 2, 3, 3, 1, 1, 1])
assert True is split_array([1, 5, 4, 3, 6, 1])

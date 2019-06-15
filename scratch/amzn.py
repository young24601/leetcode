# Given a continous stream of characters, find the first non repeating character at any given point => https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/
# Given a tree with left, right and next pointer, update next pointer to point to the right node at same level => https://leetcode.com/problems/populating-next-right-pointers-in-each-node/. Told the interviewer that I'd already done the question
# Given two arrays containing numbers, find the difference of closest greatest of each number from left and right ?
# 3 2 1 7 5
# 0 3 2 0 7 => from left (here for number 1 since 2 and 3 are both greater, we pick the closest viz. 2)
# 7 7 7 0 0 => from right
# 7 4 5 0 7 => difference


stream = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s", "a"]

stream_dict = {}

for item in stream:
    if item not in stream_dict:
        print("New", item)
        stream_dict[item] = 1
    else:
        stream_dict[item] += 1


print(stream_dict.popitem())
print(stream_dict)

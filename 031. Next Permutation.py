# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1) Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
        # 2) Find the largest index l greater than k such that a[k] < a[l].
        # 3) Swap the value of a[k] with that of a[l].
        # 4) Reverse the sequence from a[k + 1] up to and including the final element a[n].

        k = -1
        l = -1
        n = len(nums)-1
        for i in range(0, n):
            #print("comparing at", i, ":", nums[i], "<", nums[i+1], "elif", nums[k], "<", nums[i])
            if nums[i] < nums[i+1]: # 1 find largest k
                k = i
                l = i+1
            elif nums[k] < nums[i+1]: # find largest l greater than k
                l = i+1

        #print("k:", k, "l:", l, "n:", n)
        if k == -1:
            nums.sort() #1 last permutation
        else:
            #print("swapping", nums[k], "and", nums[l])
            nums[k], nums[l] = nums[l], nums[k] #3 swap a[k] and a[l]
            #print(nums)
            #print("sorting", k+1, "to", n)
            nums[k+1:] = nums[k+1:][::-1]







        print(nums)
        #print("--------------")



s = Solution()
a1 = [1,2,3,4]
print(a1)
for ct in range(0, 24):
    s.nextPermutation(a1)


print("--------------")
print([1,2,4,3])
s.nextPermutation([1,2,4,3])

# INCOMPLETE

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5


"""
Given two sorted arrays, pick the midpoint of the larger array.  In order for the solution
to be O(log(n+m)), we must divide and ignore half of the parent array.

Given two arrays, num1 and num2, if there is an odd number then the median will be the central
value.  If there is an even number, the median will be the average of the two middle values.  

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        ==
        A brute force solution would be to combine both arrays then find the median, which would be O(n+m) time.
        
        """
        len1 = len(nums1)
        len2 = len(nums2)
        
        if (len1 == 1) and (len2 == 1):
            return (nums1[0] + nums2[0])/2
        
        print 'i:', len1/2, len2/2
        #print nums1[len1/2], nums2[len2/2]
        
        

        return 'err'

###########################################3

test = Solution()

nums1 = [1]
nums2 = [5]
print 3, test.findMedianSortedArrays(nums1, nums2) #3

nums1 = [1, 3]
nums2 = [2]
print 2, test.findMedianSortedArrays(nums1, nums2) #2

nums1 = [1, 2]
nums2 = [3, 4]
print 2.5, test.findMedianSortedArrays(nums1, nums2) #2.5

nums1 = [1, 3]
nums2 = [2, 4]
print 2.5, test.findMedianSortedArrays(nums1, nums2) #2.5

nums1 = []
nums2 = [3, 4, 5]
print 4, test.findMedianSortedArrays(nums1, nums2) #4

nums1 = [3, 4]
nums2 = []
print 3.5, test.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6]
print 4, test.findMedianSortedArrays(nums1, nums2) #4

nums1 = [2, 4, 6]
nums2 = [1, 3, 5, 7]
print 4, test.findMedianSortedArrays(nums1, nums2) #4

nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7]
print 4, test.findMedianSortedArrays(nums1, nums2) #4

nums1 = [5, 6, 7]
nums2 = [1, 2, 3, 4]
print 4, test.findMedianSortedArrays(nums1, nums2) #4
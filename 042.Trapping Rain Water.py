# Given n non-negative integers representing an elevation map where the width of 
# each bar is 1, compute how much water it is able to trap after r
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
            
        # strategy take 1: 
        # fix on a height starting from the left.
        #   - if the height to the immediate right is higher (or the same), fix on that element
        #   - if the height to the immediate right is lower, then add the difference in height between the fixed element and the new element
        #     - if the height to the immediate right is higher
        print(height)
        h = height[0]
        total = 0
        local_sum = []
        for ct in range(1, len(height)):
            if height[ct] > h:
                h = height[ct]
                print 'moved fix'
                total = total + sum(local_sum)
                local_sum = []
            else:
                print 'adding ' + str(h) + ' - ' + str(height[ct])
                local_sum.append(h - height[ct])
        
        if local_sum > 0:
            print "h: " + str(h)
            print "height[ct]: " + str(height[ct])
            if height[ct] < h:
                print "removing " + str(h - height[ct]) + " from local_sum"
                local_sum = [item - (h - height[ct]) for item in local_sum]
        total = total + sum(local_sum)
        print total
        return total
        
        
        
s = Solution()

# assert 0 == s.trap([5])
# assert 0 == s.trap([1,4])
# assert 2 == s.trap([2,0,3])
# assert 2 == s.trap([2,3,1,4])
# assert 3 == s.trap([2,4,1,4])
# assert 5 == s.trap([2,4,1,2,4])
# assert 1 == s.trap([2,0,1])

assert 6 == s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
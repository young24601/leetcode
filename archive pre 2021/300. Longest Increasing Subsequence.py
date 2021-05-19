#Given an unsorted array of integers, find the length of longest increasing subsequence.

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    arr = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if (nums[j] < nums[i]):
                arr[i] = max(arr[i], arr[j]+1)

    return(max(arr))
            
print(lengthOfLIS([10,9,2,5,3,7,101,18]))


import bisect

#t = sorted([10,9,2,5,3,7,101,18])
#print(t)
#del t[bisect.bisect_left(t, 5)]
#bisect.insort(t, 4)
#print(t)

print("================================")
#print(bisect.bisect_left(t, 6))


def lengthOfLIS2(nums):
    if len(nums) == 0:
        return 0
    arr = [nums[0]]
    
    ct = 0
    length = 0
    last = nums[0]
    for i in range(1, len(nums)):
        print(nums[i], " vs ", last)
        if nums[i] > last:
            print("added ", nums[i])
            arr.append(nums[i])
            length += 1
            last = nums[i]
        else:
            print("removing ", last)
            print("left ", bisect.bisect_left(arr, last))
            print("right ", bisect.bisect_right(arr, last))
            del arr[bisect.bisect_left(arr, last, 0, length)]
            print("adding ", nums[i])
            bisect.insort(arr, nums[i])
            last = nums[i]

    print(arr)
    
# I think this is the best one...
# use bisection to find and place in log n time and place them into a list. 
# note that whenever you place a number into at the end of the list, you have increased the subsequence so increment l
# whenever you find a lower number, you place that lower number at the relevant location on
# the list.  if you are able to add more to the subsequence, then i will eventually become l and you can increment l.
# If there aren't enough to add, or if the sequence can continue by ignoring the value such as "ignoring 4" in (1,2,5,10,4,11,12)
# then your sequence is able to continue and the insertion of 4 into the list is irrelevant since you still have 10 at the "last" position
# which is what matters.
def lengthOfLIS3(nums):
    dp = [0]*len(nums)
    l = 0
    for num in nums:
        print("num =", num)
        i = bisect.bisect_left(dp, num, 0, l) #bisect_left(a, x, low, high).  Finds location for x in a to maintain sorted order.  low/high specifies subset of the list
        print("i =", i)
        dp[i] = num
        print("dp[",i,"] =", num)
        if i == l:
            l+=1
    return l
#lengthOfLIS2([1,2,3])
#lengthOfLIS2([10,9,2,5,3,7,101,18])

lengthOfLIS2([4,10,4,3,8,9])
print("==================================")
print(lengthOfLIS3([4,10,4,3,8,9]))
print("==================================")
print(lengthOfLIS3([10,9,2,5,3,7,101,18]))
print("==================================")
print(lengthOfLIS3([1,2,5,10,4,6,7,11]))

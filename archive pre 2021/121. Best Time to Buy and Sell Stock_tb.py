from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_value = prices[0]
        max_profit = 0

        for item in prices[1:]:
            if item - min_value > max_profit:
                print("setting (", item, "-", min_value, ") = ", item - min_value, "as max_profit from", max_profit)
                max_profit = item - min_value
            if item < min_value:
                print("setting new min value from", min_value, "to", item)
                min_value = item
        return max_profit


s = Solution()
assert 0 == s.maxProfit([])
assert 0 == s.maxProfit([5])
assert 5 == s.maxProfit([7,1,5,3,6,4])
assert 9 == s.maxProfit([7,1,10,9,2,4])
assert 0 == s.maxProfit([7,6,4,3,1])

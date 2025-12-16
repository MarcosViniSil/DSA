#link to problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#Time complexity: O(n)
#Space complexity: O(1)

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for current_price in prices:
            current_profit = current_price - min_price
            max_profit = current_profit if current_profit > max_profit else max_profit
            
            min_price = min_price if min_price < current_price else current_price
        
        return max_profit
        

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([7]))
print(solution.maxProfit([7,1,0,4,3,1]))
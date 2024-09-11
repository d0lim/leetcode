import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = math.inf
        current_max = 0
        for price in prices:
            if price < current_min:
                current_min = price
                current_max = 0
            else:
                current_max = max(current_max, price)
            max_profit = max(max_profit, current_max - current_min)

        return max_profit

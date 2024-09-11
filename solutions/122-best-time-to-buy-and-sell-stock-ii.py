import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        acc_profit = 0

        buy_price = math.inf
        # Find optimal profit
        for i, price in enumerate(prices):
            if i == len(prices) - 1:
                if buy_price < price:
                    acc_profit += price - buy_price
                break

            if price < buy_price and price < prices[i + 1]:
                buy_price = price
            elif buy_price < price:
                acc_profit += price - buy_price
                buy_price = price
            
        return acc_profit

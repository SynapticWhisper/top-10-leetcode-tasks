from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sub_max: int = 0
        min_price: int = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            sub_max = max(sub_max, price - min_price)
        return sub_max


    # Time limit exception
    def maxProfit_tl(self, prices: List[int]) -> int:
        sub_max = 0

        for i in range(len(prices)-1):
            profit = max(prices[i+1:]) - prices[i]
            sub_max = profit if profit > sub_max else sub_max
        return sub_max
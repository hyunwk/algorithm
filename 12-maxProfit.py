import sys
from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        max_price = 0;
        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                max_price = max(prices[j] - price, max_price)
        return max_price

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price )
        return profit

prices = [7,1,5,3,6,4]
b = Solution()
print(b.maxProfit1(prices))
print(b.maxProfit2(prices))
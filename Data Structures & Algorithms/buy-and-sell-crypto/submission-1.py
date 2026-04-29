class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float('inf')
        for price in prices:
            minPrice = min(price, minPrice)
            curSum = price-minPrice
            res = max(res, curSum)
        return res
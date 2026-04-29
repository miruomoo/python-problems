class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        high = 0

        for p in prices:
            low = min(low, p)
            high = max(high, p - low)
        
        return high
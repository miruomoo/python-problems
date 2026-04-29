class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 1

        while l<=r:
            count = 0
            mid = (l+r)//2
            for p in piles:
                count+=math.ceil(p/mid)
            if count<=h:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
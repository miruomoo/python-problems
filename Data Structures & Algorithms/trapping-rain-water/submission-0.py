class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        res = 0
        l = 0
        r = len(height)-1
        while l<r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)
            if maxL<=maxR:
                res+=min(maxL, maxR)-height[l]
                l+=1
            else:
                res+=min(maxL, maxR)-height[r]
                r-=1
        return res
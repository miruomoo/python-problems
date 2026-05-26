class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1

        for num in nums:
            if num == 0:
                curMin = 1
                curMax = 1
                continue
            temp = curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(num * temp, num * curMin, num)
            res = max(res, curMax, curMin)
        
        return res
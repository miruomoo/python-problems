class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1

        for num in nums:
            temp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, temp * num, num)

            res = max(curMax, curMin, res)

        return res
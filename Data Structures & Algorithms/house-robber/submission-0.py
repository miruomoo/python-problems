class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0
        res = 0

        for num in nums:
            res = max(num + prev2, prev)

            temp = prev
            prev = res
            prev2 = temp

        return res
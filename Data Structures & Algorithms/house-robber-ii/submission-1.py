class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.dp(1, len(nums), nums), self.dp(0, len(nums) - 1, nums))
        
    def dp(self, start, end, nums):
        rob1 = 0
        rob2 = 0

        for i in range(start, end):
            num = nums[i]
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2
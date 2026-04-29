class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finish = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            jumps = nums[i]
            if i + jumps >= finish:
                finish = i

        return True if finish == 0 else False
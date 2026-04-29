class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in hmap:
                return [hmap[comp], i]
            else:
                hmap[num] = i
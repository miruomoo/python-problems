class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            n = n & (n - 1)
            res += 1

        return res

#T: O(1)
#S: O(1)
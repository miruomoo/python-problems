class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            newN = 0
            while n:
                d = n % 10
                newN += d ** 2
                n = n // 10
            if newN in seen:
                return False
            seen.add(newN)
            n = newN
        
        return True


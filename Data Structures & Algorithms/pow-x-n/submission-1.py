class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def fastPow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = fastPow(x * x, n // 2)
            
            return x * res if n % 2 else res

        newN = abs(n)
        return fastPow(x, newN) if n >= 0 else 1 / fastPow(x, newN)
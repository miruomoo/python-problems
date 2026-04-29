class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []

        for q in queries:
            minLength = float('inf')
            for start, end in intervals:
                if start <= q <= end:
                    minLength = min(minLength, end - start + 1)
            if minLength == float('inf'):
                res.append(-1)
            else:
                res.append(minLength)

        return res



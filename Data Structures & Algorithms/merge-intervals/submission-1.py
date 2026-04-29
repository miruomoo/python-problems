class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        res = [intervals[0]]

        for interval in intervals:

            start, end = interval

            if start > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
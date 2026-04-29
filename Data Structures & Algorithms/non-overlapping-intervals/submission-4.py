class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        lastEnd = intervals[0][1]

        for interval in intervals[1:]:
            start, end = interval
            if start >= lastEnd:
                lastEnd = end
            else:
                res += 1
                lastEnd = min(end, lastEnd)

        return res
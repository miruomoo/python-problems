class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        res = [intervals[0]]

        for interval in intervals[1:]:
            start, end = interval
            lastEnd = res[-1][1]

            if start > lastEnd:
                res.append(interval)
            else:
                res[-1][1] = max(lastEnd, end)
        
        return res
            
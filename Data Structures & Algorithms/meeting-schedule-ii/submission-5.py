"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1

        startTimes = sorted([interval.start for interval in intervals])
        endTimes = sorted([interval.end for interval in intervals])

        start = end = 0
        res = curMax = 0

        while start < len(intervals):
            startTime, endTime = startTimes[start], endTimes[end]

            if startTime < endTime:
                start += 1
                curMax += 1
            else:
                end += 1
                curMax -= 1

            res = max(curMax, res)

        return res
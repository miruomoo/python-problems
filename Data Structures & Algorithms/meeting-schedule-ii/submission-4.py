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

        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])

        res = 0
        curMax = 0

        start = 0
        end = 0

        while start < len(intervals):
            startTime = startTimes[start]
            endTime = endTimes[end]

            if startTime < endTime:
                start += 1
                curMax += 1
            else:
                end += 1
                curMax -= 1

            res = max(res, curMax)

        return res
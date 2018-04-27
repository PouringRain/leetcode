# level: medium

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals.sort(key=lambda interval: interval.start)
        # print intervals
        res = []
        for i in range(0, len(intervals)):
            if not res or res[-1].end < intervals[i].start:
                # 合并
                res.append(intervals[i])
            else:
                if res[-1].end < intervals[i].end:
                    res[-1].end = intervals[i].end

        return res
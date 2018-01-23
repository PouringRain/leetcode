# level: medium
# solution: greedy algorithm

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == []: return 0
        ans = 0
        intervals.sort(key=lambda x: (x.end))
        # for i in range(len(intervals)):
        #     print intervals[i].end
        end = intervals[0].end

        for i in range(len(intervals)):
            if end <= intervals[i].start:
                end = intervals[i].end
            else:
                ans += 1

        return ans - 1

if __name__ == '__main__':
    ans = Solution()
    intervals = []
    intervals.append(Interval(1,2))
    intervals.append(Interval(2,3))
    intervals.append(Interval(3,4))
    intervals.append(Interval(1,3))
    print(ans.eraseOverlapIntervals(intervals))
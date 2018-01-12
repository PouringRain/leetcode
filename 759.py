# level: hard
# 思路：先按开始时间排序，然后在建立栈判断栈顶结束时间和新来的开始时间的关系，更新结果

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def employeeFreeTime(self, schedule):
        import itertools
        schedule = list(sorted(itertools.chain(*schedule), key=lambda interval: interval.start))

        stack = [schedule[0]]
        result = []

        for s in schedule:
            top = stack.pop()
            if top.end < s.start:
                result.append([top.end, s.start])
                stack.append(s)
            else:
                if top.end >= s.end:
                    stack.append(top)
                else:
                    stack.append(s)

        return result
# level: medium
# solution : find Invariant

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace('X', '') != end.replace('X', ''):
            return False
        t = 0
        for i in range(len(start)):
            if start[i] == 'L':
                while end[t] != 'L': t += 1
                if t > i:
                    return False
                t += 1
        t = 0
        for i in range(len(start)):
            if start[i] == 'R':
                while end[t] != 'R': t += 1
                if t < i:
                    return False
                t += 1

        return True


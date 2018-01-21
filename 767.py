# level: medium
# solution: priority quene
from collections import Counter
import heapq


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        c = Counter(S)
        pq = []
        s = ''
        # print c
        for k, v in c.items():
            heapq.heappush(pq, (-v, k))
        aa, bb = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            s += b
            if aa < 0:
                heapq.heappush(pq, (aa, bb))
            a += 1

            aa, bb = a, b

        # print s
        if len(s) == len(S):
            return s
        else:
            return ''

if __name__ == '__main__':
    ans = Solution()
    print(ans.reorganizeString('aab'))
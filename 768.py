# level: hard

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        c1, c2 = collections.Counter(), collections.Counter()
        nowMax = -1
        l = sorted(arr)
        for a, b in zip(arr, l):
            c1[a] += 1
            c2[b] += 1
            if c1 == c2:
                ans += 1

        return ans
# level: eazy

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) < 3: return []
        res = []
        # two pointers
        p = q = 0
        while q < len(S):
            if S[p] == S[q]:
                if q == len(S) - 1 and q - p >= 2:
                    res.append([p, q])

                q += 1
                # 如果不相等
            else:
                if q - p >= 3:
                    res.append([p, q - 1])
                p = q

        return res
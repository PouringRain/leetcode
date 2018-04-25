# level: eazy

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        lenth = len(S)
        for i, c in enumerate(S):
            # 双指针飞起来
            p = q = i
            minleft = minright = 10000
            while p >= 0:
                if S[p] == C:
                    minleft = i - p
                    break
                p -= 1
            while q < lenth:
                if S[q] == C:
                    minright = q - i
                    break
                q += 1

            res.append(min(minleft, minright))

        return res
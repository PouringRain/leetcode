# level: eazy

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ans, lenth = 0, len(points)

        def getArea(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)

        for i in range(lenth - 2):
            for j in range(i + 1, lenth - 1):
                for k in range(j + 1, lenth):
                    ans = max(ans, getArea(points[i], points[j], points[k]))

        return ans
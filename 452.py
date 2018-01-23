# level: medium
# solution: greedy algorithm
# 按end排序，如果start在end前则可以一起扎破气球，否则开启一个新的区间

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points == []: return 0

        ans = 1
        points.sort(key=lambda x: (x[1]))
        # print points
        # start, end = [], []
        # for point in points:
        #     start.append(point[0])
        #     end.append(point[1])
        lastend = points[0][1]
        for i, point in enumerate(points):
            if lastend < point[0]:
                ans += 1
                lastend = point[1]

        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
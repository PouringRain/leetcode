# level:medium
# 思路：说实话参考discuss中大神的算法，按行遍历，flag数组记录i,j列都是1的个数。

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0

        flag = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(0, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == 1:
                    for k in range(0, j):
                        if grid[i][k] == 1:
                            result += flag[k][j]
                            flag[k][j] += 1

        return result

if __name__ == '__main__':
    ans = Solution()
    print(ans.countCornerRectangles([[0,1,0],[1,0,1],[1,0,1],[0,1,0]]))

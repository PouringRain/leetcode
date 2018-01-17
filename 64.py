# level: medium
# 思路: dp
# Your runtime beats 47.20 % of python submissions

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        cache = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    cache[i][j] = min(cache[i][j - 1], cache[i - 1][j]) + grid[i][j]
                elif i == 0 and j > 0:
                    cache[i][j] = cache[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    cache[i][j] = cache[i - 1][j] + grid[i][j]
                else:
                    cache[i][j] = grid[i][j]

        return cache[-1][-1]

if __name__ == '__main__':
    ans = Solution()
    print(ans.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
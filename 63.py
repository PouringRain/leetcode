# level: medium
# Your runtime beats 61.37 % of python submissions.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        cache = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    if obstacleGrid[i][j]==1:
                        cache[i][j]=0
                    else:
                        cache[i][j] = cache[i][j-1]+cache[i-1][j]
                elif i == 0 and j > 0:
                    if obstacleGrid[i][j]==1:
                        cache[i][j]=0
                    else:
                        cache[i][j] = cache[i][j-1]
                elif j == 0 and i > 0:
                    if obstacleGrid[i][j]==1:
                        cache[i][j]=0
                    else:
                        cache[i][j] = cache[i-1][j]
                else:
                    if obstacleGrid[i][j]==1:
                        cache[i][j]=0
                    else:
                        cache[i][j]=1

        return cache[-1][-1]

if __name__ == '__main__':
    ans = Solution()
    print(ans.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
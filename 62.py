# level: medium
# Your runtime beats 29.74 % of python submissions.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
                elif i == 0 and j > 0:
                    cache[i][j] += 1
                elif j == 0 and i > 0:
                    cache[i][j] += 1
                else:
                    cache[i][j] = 1

        return cache[-1][-1]

if __name__ == '__main__':
    ans = Solution()
    print(ans.uniquePaths(3,4))
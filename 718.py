class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for col in range(len(A) + 1)] for row in range(len(B) + 1)]
        # print dp
        ans = 0
        for i in range(len(B)):
            for j in range(len(A)):
                if A[j] == B[i]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    ans = max(ans, dp[i + 1][j + 1])

        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.findLength([1,2,3,2,1],[3,2,1,4,7]))
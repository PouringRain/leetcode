class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)
        dp = [[0 for i in range(size2+1)] for j in range(size1+1)]
        
        for i in range(size2+1):
            dp[0][i] = i
        for i in range(size1+1):
            dp[i][0] = i
        for i in range(1, size1+1):
            for j in range(1, size2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, 1+min(dp[i-1][j], dp[i][j-1]))
                    
        return dp[-1][-1]

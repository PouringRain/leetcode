class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l_cost = len(cost)
        if l_cost <= 1: return 0
        dp = [0] * l_cost
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, l_cost):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])

if __name__ == '__main__':
    ans = Solution()
    print(ans.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

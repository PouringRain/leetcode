# level: eazy

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = float('inf')
        profit = 0
        for i in range(len(prices)):
            # low = min(low, prices[i])
            if low >= prices[i]:
                low = prices[i]
            elif prices[i] - low > profit:
                profit = prices[i] - low

        return profit
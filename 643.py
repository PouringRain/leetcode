# level: eazy

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s, m = 0, 0
        l_nums = len(nums)
        if k == 1: return max(nums)

        for i in range(k):
            m += nums[i]
            s += nums[i]

        for i in range(1, l_nums - k + 1):
            s = s + nums[i + k - 1] - nums[i - 1]
            if m < s:
                m = s

        return m / (k * 1.0)

if __name__ == '__main__':
    ans = Solution()
    print(ans.findMaxAverage([1,12,-5,-6,50,3], 4))

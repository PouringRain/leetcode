# level: eazy
# 思路：以i结尾的子串为，若i之前子串为负则子串为i，否则为子串+i

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, max_sub = nums[0], nums[0]
        for i in range(1, len(nums)):
            if total<=0:
                total = nums[i]
            else:
                total += nums[i]
            if max_sub<total:
                max_sub = total
        return max_sub

if __name__ == '__main__':
    ans = Solution()
    print(ans.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
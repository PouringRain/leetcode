# level: medium

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]: return 0
        # 每个以i结尾的最大递增长度
        cache = [1]*len(nums)
        count = [1]*len(nums)
        for i in range(len(nums)):
            m = 1
            for j in range(i):
                if nums[j]<nums[i]:
                     if m<cache[j]+1:
                        m = cache[j]+1
                        count[i] = count[j]
                     elif m==cache[j]+1:
                        count[i]+=count[j]
            cache[i] = m
        # print(cache)
        # print(count)
        m = max(cache)
        ans = 0
        for i in range(len(nums)):
            if cache[i]==m:
                ans += count[i]
        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.findNumberOfLIS([1,2,4,3,5,4,7,2]))
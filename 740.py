# coding=utf-8

#level: Medium
# 思路：dp

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, earn = [0]*20000, [0]*20000
        len_nums = len(nums)
        for i in range(len_nums):
            a[nums[i]] += 1

        for i in range(1, len(a)):
            earn[i] = max(earn[i-1], earn[i-2]+a[i]*i)


        return max(earn)

if __name__ == '__main__':
    ans = Solution()
    print(ans.deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(ans.deleteAndEarn([4, 10, 10, 8, 1, 4, 10, 9, 7, 6]))

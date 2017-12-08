# coding=utf-8

#difficult: Medium
# 题目：增加减少数，求最大赚取金额
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

        earn[1] = a[1]
        earn[2] = a[2]*2
        earn[3] = max(earn[1]+3*a[3], earn[2])

        for i in range(4, len(a)):
            earn[i] = max(earn[i-1], max(earn[i-2]+a[i]*i, earn[i-3]+a[i]*i))


        return max(earn)

if __name__ == '__main__':
    ans = Solution()
    print(ans.deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(ans.deleteAndEarn([4, 10, 10, 8, 1, 4, 10, 9, 7, 6]))

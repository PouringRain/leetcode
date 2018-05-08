# level: eazy
# solution: 递归

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, res, cur, rest):
            # cur:当前结果
            # rest: 剩余可选择数字
            if cur == []: rest = nums
            if len(cur) == len(nums):
                res.append(cur)

            for i in range(len(rest)):
                dfs(nums, res, cur + [rest[i]], rest[0:i] + rest[i + 1:])

        dfs(nums, res, [], [])

        return res

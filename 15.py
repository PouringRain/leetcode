# level: medium
# solution: tow pointers

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 去重

        nums.sort()
        # print nums
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p, q = i + 1, len(nums) - 1
            while p < q:
                x = nums[i] + nums[p] + nums[q]
                if x == 0:
                    res.append([nums[i], nums[p], nums[q]])
                    while p < q and nums[p + 1] == nums[p]:
                        p += 1
                    while p < q and nums[q - 1] == nums[q]:
                        q -= 1
                        # p+=1;q-=1
                if x < 0:
                    p += 1
                else:
                    q -= 1

        return res
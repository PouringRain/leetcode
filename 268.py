# level: eazy

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0] * (len(nums) + 1)

        for num in nums:
            count[num] = 1

        return count.index(0)

if __name__=='__main__':
    ans = Solution()
    print(ans.missingNumber([1,0,3]))
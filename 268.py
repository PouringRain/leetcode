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
    
    
# level: ez
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i]<len(nums) and nums[nums[i]]!=nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
        

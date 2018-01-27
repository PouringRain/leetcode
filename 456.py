# level: medium
# solution: 栈存放比三个数大的数，如果nums[i]<third，return True，否则
#           遍历栈顶使栈顶的数大于c，实际只用到了栈顶

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        stack = []
        c = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < c:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    c = stack.pop()
                stack.append(nums[i])

        return False

if __name__ == '__main__':
    ans = Solution()
    print(ans.find132pattern([1,2,4,3]))
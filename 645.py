
# level: easy

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        len_nums = len(nums)
        a = [0] * (len_nums + 1)

        for i in range(0, len_nums):
            a[nums[i]] += 1
        for i in range(1, len_nums + 1):
            if a[i] == 2:
                dup = i
            if a[i] == 0:
                missing = i

        result.append(dup)
        result.append(missing)

        return result

if __name__ == '__main__':
    ans = Solution()
    print(ans.findErrorNums([1,2,2,4]))

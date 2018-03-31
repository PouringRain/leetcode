# level: hard
# solution: 桶排序

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0

        minNum, maxNum = min(nums), max(nums)
        bucketrange = max(1, ((maxNum - minNum-1) / (len(nums)-1) + 1))
        lenth = (maxNum-minNum)/bucketrange + 1

        buckets = [[None, None] for i in range(lenth)]
        # print buckets
        for num in nums:
            i = (num - minNum) / bucketrange

            if buckets[i][0] == buckets[i][1] == None:
                buckets[i][0] = buckets[i][1] = num
            else:
                if buckets[i][0] > num:
                    buckets[i][0] = num
                if buckets[i][1] < num:
                    buckets[i][1] = num
        # print buckets

        gap, pre = -1, 0
        for i in range(0, len(buckets)):
            if buckets[i] == [None, None]:
                continue
            else:
                gap = max(gap, buckets[i][0] - buckets[pre][1])
                pre = i

        return gap

if __name__=='__main__':
    ans = Solution()
    print(ans.maximumGap([1, 1000000]))
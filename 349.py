# level: eazy

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = set()
        for num in nums1:
            if num in nums2:
                ans.add(num)
        return list(ans)
if __name__=='__main__':
    ans = Solution()
    print(ans.intersection([1,2,3],[2,4,5]))
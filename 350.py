# level: eazy

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums1:
            if num in nums2:
                nums2.remove(num)
                ans.append(num)
        return ans
if __name__=='__main__':
    ans = Solution()
    print(ans.intersect([1,2,2,1], [2]))
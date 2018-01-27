# level: medium

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0
        N = len(A)
        aa, bb = [], []

        for i in range(N):
            for j in range(N):
                aa.append(A[i] + B[j])
                bb.append(C[i] + D[j])

        a, b = collections.Counter(aa), collections.Counter(bb)

        for key in a:
            if b.has_key(0 - key):
                ans += a[key] * b[0 - key]

        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.fourSumCount([1,2]
[-2,-1]
[-1,2]
[0,2]))
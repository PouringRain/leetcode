class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if K==1: return 0
        elif K==2: return 1
        elif K%2==1:
            return self.kthGrammar(N, (K+1)//2)
        else:
            return 1-self.kthGrammar(N, K//2)
        

if __name__ == '__main__':
    ans = Solution()
    print(ans.kthGrammar(3,3))

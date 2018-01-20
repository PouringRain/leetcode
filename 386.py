# level: medium
# 回溯

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        def dfs(now, n):
            if now > n:
                return
            else:
                res.append(now)
                for i in range(10):
                    if 10 * now + i > n:
                        return
                    else:
                        dfs(10 * now + i, n)

        for i in range(1, 10):
            dfs(i, n)
        return res

if __name__ == '__main__':
    ans = Solution()
    print(ans.lexicalOrder(25))
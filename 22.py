# level: medium
# solution:
#        1, 当left=0&&right=0时表示找到一条路径
#        2, 当left!=0时可以向左子树伸展
#        3, 当right!=0&&left< right时可以向右子树伸展


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def gen(l, r, path, res):
            if l == r == 0:
                res.append(path)
                return
            if l != 0:
                gen(l - 1, r, path + '(', res)
            if r != 0 and l < r:
                gen(l, r - 1, path + ')', res)

        gen(n, n, '', res)

        return res
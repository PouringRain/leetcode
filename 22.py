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
    
# level: medium
# solution: 
#        1. 选择 加left/right
#        2. 条件 left>0加左边 right>left加右边
#        3. 结束 left=right=0  


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def traceback(path, left, right, res):
            if left==right==0:
                res.append(path)
                return
            if left>0:
                traceback(path+'(', left-1, right, res)
            if right>left:
                traceback(path+')', left, right-1, res)
        traceback('', n, n, res)
        
        return res

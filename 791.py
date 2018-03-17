class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        c = collections.Counter(T)
        ans = []
        
        for w in S:
            ans.append(w * c[w])
            c[w] = 0
        for k, v in c.items():
            if c[k]:
                ans.append(k * v)

        return ''.join(ans)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        if len(strs)==1: return strs[0]
        ret, pos = [], 0
        strs = sorted(strs, key=lambda x:len(x), reverse=False)
        size = len(strs[0])
        find = 0
        
        while size>0:
            if find: break
            for i in range(1, len(strs)):
                if strs[i][pos]!=strs[i-1][pos]:
                    find = 1
                    break
                if i==len(strs)-1:
                    ret.append(strs[i][pos])
                    pos+=1
            
            size-=1
            
        return ''.join(ret)

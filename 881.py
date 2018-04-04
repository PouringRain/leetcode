# level: eazy

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        res = []
        for cpdomain in cpdomains:
            num_domain = cpdomain.split(' ')
            num, domain = int(num_domain[0]), num_domain[1]
            levels = domain.split('.')
            level, i = levels[-1], len(levels) - 1
            while i >= 0:
                if d.has_key(level):
                    d[level] += num
                else:
                    d[level] = num
                level = levels[i - 1] + '.' + level
                i -= 1

        for k, v in d.items():
            res.append(str(v) + ' ' + k)

        return res
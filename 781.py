# level: medium

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        la, ans = len(answers), 0
        if la == 0: return 0
        if la == 1: return answers[0] + 1
        c = collections.Counter(answers)
        for k, num in c.items():
            if num == 1:
                ans += k + 1
            else:
                if num % (k + 1) == 0:
                    group = num // (k + 1)
                else:
                    group = num // (k + 1) + 1
                ans += group * (k + 1)

        return ans

if __name__ == '__main__':
    ans = Solution()
    print(ans.numRabbits([0,0,1,1,1]))
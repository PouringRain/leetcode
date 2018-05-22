# level: medium
# solution: nice queue solution but what a pity  also tle...
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        import Queue
        q = Queue.Queue()
        lenth = len(dominoes)
        dominoes = list(dominoes)
        for i in range(lenth):
            if dominoes[i] in ['L', 'R']:
                q.put(i)
        while not q.empty():
            i = q.get()
            if dominoes[i] == 'L':
                if i == 0: continue
                if dominoes[i - 1] != '.': continue
                if i - 2 >= 0 and dominoes[i - 2] == 'R': continue
                dominoes[i - 1] = 'L'
                q.put(i - 1)
            if dominoes[i] == 'R':
                if i == lenth - 1: continue
                if dominoes[i + 1] != '.': continue
                if i + 2 < lenth and dominoes[i + 2] == 'L': continue

                dominoes[i + 1] = 'R'
                q.put(i + 1)
                if i + 3 < lenth and dominoes[i + 3] == 'L' and dominoes[i + 2] == '.':
                    dominoes[i + 2] = 'L'
                    q.put(i + 2)

        return ''.join(dominoes)


'''
# funny solution! but TLE...
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        while True:
            print dominoes
            new = dominoes.replace('R.L', 'S').replace('.L', 'LL').replace('R.', 'RR')
            if dominoes==new:
                break
            else:
                dominoes = new

        return dominoes.replace('S', 'R.L')
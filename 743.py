class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # [[2,1,1],[2,3,1],[3,4,1]]

        # nodes = [[0]*(N+1)]*(N+1)  浅拷贝，别这么赋值
        nodes = [[-1 for i in range(N + 1)] for i in range(N + 1)]
        NUM = 100000
        dis = [NUM] * (N + 1)
        dis[K] = 0
        len_times = len(times)
        # neighbor matrix
        for i in range(len_times):
            time = times[i]
            nodes[time[0]][time[1]] = time[2]
        print nodes
        q = set(range(1, N + 1))
        while len(q):
            u = None
            for node in q:
                if u == None or dis[node] < dis[u]:
                    u = node

            q.remove(u)
            for v, uv in enumerate(nodes[u]):
                if uv != -1:
                    m = uv + dis[u]
                    dis[v] = min(dis[v], m)

        if max(dis[1:]) != NUM:
            return max(dis[1:])
        else:
            return -1

if __name__ == '__main__':
    ans = Solution()
    print(ans.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
# level: medium
# 思路： h降序排序，k升序排序，再插入

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        def my_way(people):

            return -people[0], people[1]

        people.sort(key=my_way)
        result = []
        for p in people:
            result.insert(p[1], p)

        return result

if __name__ == '__main__':
    ans = Solution()
    print(ans.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
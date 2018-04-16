# level: medium
# getattr(object, 成员, 默认值) return 属性值
# 能set就set

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        ans = 0
        p = head
        while p:
            if p.val in g and getattr(p.next, 'val', None) not in g:
                ans += 1

            p = p.next
        return ans
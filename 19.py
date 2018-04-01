# level: medium
# solution: tow pointers
#           要求一次遍历。指针1初始化为head位置，指针2向前移动n的位置...

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = q = head

        for i in range(n):
            q = q.next
        if q == None:
            return head.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head
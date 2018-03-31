# level : eazy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        p, q = headA, headB
        lenA, lenB = 0, 0
        while p.next:
            p = p.next
            lenA += 1
        while q.next:
            q = q.next
            lenB += 1
        if p != q:
            return None

        if lenA >= lenB:
            p, q = headA, headB
        else:
            p, q = headB, headA
        margin = abs(lenA - lenB)
        for _ in range(margin):
            p = p.next
        while p != q:
            p = p.next
            q = q.next

        return p
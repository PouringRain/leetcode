# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(None)
        pointer = res
        pp = pointer

        def getLen(l):
            r, rl = l, 1
            while r.next:
                rl += 1
                r = r.next
            return rl

        if getLen(l1) <= getLen(l2):
            p, q = l1, l2
        else:
            p, q = l2, l1

        l = getLen(q)

        i, t = 0, 0
        while t or i < l:
            if not p:
                pv = 0
            else:
                pv = p.val
            if not q:
                qv = 0
            else:
                qv = q.val
            k = pv + qv + t
            if k > 9:
                k = k % 10
                t = 1
            else:
                t = 0
            if p: p = p.next
            if q: q = q.next
            pp.val = k
            pp.next = ListNode(None)
            pp = pp.next
            i += 1
        pp = pointer
        while pp.next.val != None:
            pp = pp.next
        pp.next = None

        return pointer

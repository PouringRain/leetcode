# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return None
        if head.next == None: return None
        # p每次走一步 q每次走两步
        p, q = head, head
        while q != None:
            q = q.next
            if p == q:
                return p
            else:

                if q == None:
                    return None
                else:
                    q = q.next
                    p = p.next

        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        meet = self.hasCycle(head)

        if meet != None:
            p = head
            meet = meet.next
            while p != meet:
                p = p.next
                meet = meet.next
            return p
        else:
            return None
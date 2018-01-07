# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        oh = head  # odd head
        eh = head.next  # even head
        q, r = oh, eh
        p = eh.next
        while p:
            q.next = p
            q = q.next
            p = p.next
            r.next = p
            if r.next:
                r = r.next
                p = p.next
            else:
                break

        q.next = eh

        return oh
# level: medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = {}
        p = head
        while p:
            if count.has_key(p.val):
                count[p.val]+=1
            else:
                count[p.val] = 1
            p = p.next
        print count
        
        newH = ListNode(0)
        newH.next = None
        q = newH
        p = head
        
        while p:
            if count[p.val]==1:
                q.next = p
                q = p
                p = p.next
                q.next = None
            else:
                p = p.next
            
            
        
        return newH.next
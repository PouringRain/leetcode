# level: eazy
# solution1: recursively
# solution2: stack

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        import Queue
        q = Queue.Queue()
        q.put(root)
        q.put(root)
        while not q.empty():
            t1 = q.get()
            t2 = q.get()
            if t1 == None and t2 == None: continue
            if (t1 == None or t2 == None): return False
            if t1.val != t2.val: return False

            q.put(t1.left)
            q.put(t2.right)
            q.put(t1.right)
            q.put(t2.left)

        return True


'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.mirror(root.left, root.right)
    def mirror(self, t1, t2):
        if t1==None and t2==None: return True
        if (t1==None or t2==None): return False
        if t1.val==t2.val:
            return self.mirror(t1.left, t2.right) and self.mirror(t1.right, t2.left)
        else: return False
'''
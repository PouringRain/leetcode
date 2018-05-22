# level: eazy
# solution: 比较位置

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        bx1, by1 = rec1[0], rec1[1]
        tx1, ty1 = rec1[2], rec1[3]

        bx2, by2 = rec2[0], rec2[1]
        tx2, ty2 = rec2[2], rec2[3]

        if by2 >= ty1 or bx2 >= tx1 or ty2 <= by1 or tx2 <= bx1:
            return False
        else:
            return True
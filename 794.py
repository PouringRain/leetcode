# level: medium


class Solution(object):
    def judge(self, a, c):
        if a[0][0] == a[0][1] == a[0][2] == c:
            return False
        elif a[2][0] == a[2][1] == a[2][2] == c:
            return False
        elif a[0][0] == a[0][1] == a[0][2] == c:
            return False
        elif a[0][0] == a[1][0] == a[2][0] == c:
            return False
        elif a[0][0] == a[1][1] == a[2][2] == c:
            return False
        elif a[0][2] == a[1][1] == a[2][0] == c:
            return False
        else:
            return True

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        nx, no = 0, 0
        for s in board:
            for c in s:
                if c == 'X':
                    nx += 1
                elif c == 'O':
                    no += 1
        if nx < no or nx - no > 1:
            return False
        elif nx == no:
            return self.judge(board, 'X')
        else:
            return self.judge(board, 'O')

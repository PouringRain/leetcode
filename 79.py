# level: medium
# solution: backtracking

class Solution(object):
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # 回溯
        def backtracking(board, row, col, cur, now, lenth, count):
            '''
            row: 当前行
            col: 当前列
            cur: 当前存储的找到的序列
            now: 当前要查找的char的index
            '''
            # print cur

            if len(cur) == lenth: return True
            for i, j in zip(self.x, self.y):
                if 0 <= i + row < len(board) and 0 <= j + col < len(board[0]) \
                        and count[i + row][j + col] == 0 and board[i + row][j + col] == word[now]:
                    count[row][col] = 1
                    if backtracking(board, i + row, j + col, cur + [word[now]], now + 1, lenth, count):
                        return True
                    count[row][col] = 0

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    count = [[0 for col in range(len(board[0]))] for row in range(len(board))]
                    count[i][j] = 1
                    if backtracking(board, i, j, [word[0]], 1, len(word), count):
                        return True

        return False
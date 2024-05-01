class Solution:
    def solveNQueens(self, n: int):
        result = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(n, 0, chessboard, result)
        return result
    
    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append(chessboard[:])
            return
        
        for col in range(n):
            if self.isValid(col, row, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col + 1:]
                self.backtracking(n, row + 1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col + 1:]
    
    def isValid(self, col, row, chessboard):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        
        i, j = row - 1, col - 1
        while (i >= 0) and (j >= 0):
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        i, j = row - 1, col + 1
        while (i >= 0) and (j < len(chessboard)):
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True




        
    
result = Solution()
n = 4
print(result.solveNQueens(n))
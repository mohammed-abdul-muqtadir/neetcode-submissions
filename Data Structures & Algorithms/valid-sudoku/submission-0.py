class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRow(i,j,board):
            for k in range(9):
                if k != j:
                    if board[i][k] == board[i][j]:
                        return True
        
        def checkColoum(i,j,board):
            for k in range(9):
                if k != i:
                    if board[k][j] == board[i][j]:
                        return True
        
        def checkBox(i,j,board):
            startr = (i//3) * 3
            startc = (j//3) * 3
            for k in range(startr,startr+3):
                for l in range(startc,startc+3):
                    if i!=k or j != l:
                        if board[k][l] == board[i][j]:
                            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if checkRow(i,j,board) or checkColoum(i,j,board) or checkBox(i,j,board):
                        return False
        
        return True
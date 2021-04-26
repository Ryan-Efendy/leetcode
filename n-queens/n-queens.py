from copy import deepcopy

class Solution:
    def solveNQueens(self, n):
        """
        create the empty n*n board
        """
        board = [["."]*(n) for _ in range(n)]
        queens = []
        
        def isValid(location, queens):
            row, col = location
            for queen in queens:
                x, y = queen
                if abs(row - x) == abs(col - y):
                    return False
                if row == x or col == y:
                    return False
            return True

        def backtrack(board, row, ans):
            """
            add to the solution if all the N queens are placed successfully
            """
            if row == len(board):
                # Both list(...) and arr[:] are shallow not deep copy
                ans.append(deepcopy(board))
                return ans

            for col in range(len(board)):
                """
                check if a Queen is present in diagonal, anti-diagonal, row or column of the cell you are lookin to place a Queen
                """
                # _anti_diag = [board[i][col+row-i] for i in range(len(board)) if col+row-i < len(board) and col+row-i >= 0]
                # _diag = [board[i][col-row+i] for i in range(len(board)) if col-row+i < len(board) and col-row+i >= 0]
                # _row = [board[row][i] for i in range(len(board))]
                # _col = [board[i][col] for i in range(len(board))]
                
                if isValid((row, col), queens):

                # if max(_anti_diag) == "." and max(_diag) == "." and max(_row) == "." and max(_col) == ".":
                    """
                    place the queen
                    """
                    board[row][col] = "Q"
                    queens.append((row, col))

                    """
                    explore to place the next queen
                    """
                    backtrack(board, row+1, ans)

                    """
                    remove the queen; backtrack and continue the exploration
                    """
                    board[row][col] = "."
                    queens.remove((row, col))

            return ans

        """
        output the result in the required format
        """
        return [[''.join(_) for _ in __] for __ in backtrack(board, 0, [])]
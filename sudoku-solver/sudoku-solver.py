class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Check if digit can be placed at position (row,col)
        def is_valid(digit, row, col):
            # check row
            for y in range(len(board)):
                if board[row][y] == str(digit):
                    return False
            # check column
            for x in range(len(board)):
                if board[x][col] == str(digit):
                    return False
            # check square
            square_x, square_y = row//3, col//3
            for x in range(square_x*3, square_x*3+3):
                for y in range(square_y*3, square_y*3+3):
                    if board[x][y] == str(digit):
                        return False
            return True

        # Find a valid digit for position (row, col), if possible, and recurse / backtrack
        def backtrack(row, col):
            # goal
            if row == len(board):
                return True
            elif col == len(board): 
                return backtrack(row+1, 0)  # go to next row
            if board[row][col] == ".":
                for digit in range(1, 10):
                    if is_valid(digit, row, col): # constraint
                        board[row][col] = str(digit) # choose
                        if backtrack(row, col+1):  # explore
                            return True
                        board[row][col] = "." # unchoose
                return False
            else:
                return backtrack(row, col+1) # go to next col

        backtrack(0,0)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            r = set()
            for col in row:
                if col == '.': continue
                if col in r: return False
                r.add(col)
        
        # check columns
        for i in range(len(board)):
            c = set()
            for j in range(len(board[i])):
                if board[j][i] == '.': continue
                if board[j][i] in c: return False
                c.add(board[j][i])
        
        # check sub-boxes            
        for x in [0,3,6]:
            # print('x',x)
            for y in [0,3,6]:
                # print('y',y)
                box = set()
                for i in range(0,3):
                    for j in range(0,3):
                        # print(i+x,j+y)
                        if board[i+x][j+y] == '.': continue
                        if board[i+x][j+y] in box: return False
                        box.add(board[i+x][j+y])
        
        return True

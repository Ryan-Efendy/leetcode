class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m - row, n - col
        # m, n = len(matrix), len(matrix[0])
        res = []
        
        while len(matrix) > 0 and len(matrix[0]) > 0:
            # first row
            for i in range(len(matrix[0])):
                res.append(matrix[0][i])
            matrix.pop(0)
​
            if len(matrix) > 0 and len(matrix[0]) > 0:
                # last column
                for i in range(len(matrix)):
                    res.append(matrix[i][-1])
                    matrix[i].pop(-1)
​
            if len(matrix) > 0 and len(matrix[0]) > 0:
                # last row
                for i in range(len(matrix[0])-1,-1,-1):
                    res.append(matrix[-1][i])
                matrix.pop(-1)
​
            if len(matrix) > 0 and len(matrix[0]) > 0:
                # first column
                for i in range(len(matrix)-1,-1,-1):
                    res.append(matrix[i][0])
                    matrix[i].pop(0)
​
        return res
    
        '''
        [1,2,3,3,6,9,9,8,7,7,4,1]
                             ^
        '''

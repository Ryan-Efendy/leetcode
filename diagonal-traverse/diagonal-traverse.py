class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        n = len(matrix) # row
        m = len(matrix[0]) # col
        d = {}
        for i in range(n):
            # intermediate = []
            for j in range(m):
                if i+j in d:
                    d[i+j] = d.get(i+j) + [matrix[i][j]]
                else:
                    d[i+j] = [matrix[i][j]]
        
        res = []
        for i in range(n+m-1):
            if i % 2 == 0:
                res.extend(d[i][::-1])
            else:
                res.extend(d[i])
        return res

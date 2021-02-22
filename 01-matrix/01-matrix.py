class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not len(matrix): return matrix
        m, n = len(matrix), len(matrix[0])
        q = collections.deque()
        visitted = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    visitted.add((i, j))
        
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]
        while q:
            size = len(q)
            for _ in range(size):
                x1, y1 = q.popleft()
                for x, y in directions:
                    x2, y2 = x1 + x, y1 + y
                    if x2 >= 0 and x2 < m and y2 >= 0 and y2 < n and (x2, y2) not in visitted:
                        matrix[x2][y2] = matrix[x1][y1] + 1
                        q.append((x2, y2))
                        visitted.add((x2, y2))
        return matrix
                        
        
        
class Solution:
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    q = None
    visitted = None
    res = None
    
    def numIslands(self, grid: List[List[str]]) -> int:        
        if not grid or not len(grid) or not len(grid[0]): return 0
        self.q = collections.deque()
        self.visitted = set()
        self.res = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in self.visitted:
                    self.q.append((i, j))
                    self.bfs(grid, i, j)
                    self.res += 1
        return self.res
        
        
    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        while self.q:
            i, j = self.q.popleft()
            for direction in self.directions:
                x, y = i + direction[0], j + direction[1]
                if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in self.visitted and grid[x][y] == '1':
                    self.q.append((x, y))
                    self.visitted.add((x, y))

                    
                        
                    
    
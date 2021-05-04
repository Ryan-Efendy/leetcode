class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        similar to As Far from Land as Possible
        
        0: empty cell,
        1: fresh orange
        2: rotten orange
        '''
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visitted = set()
        level, freshCount = 0, 0
        
        for i in range(m):
            for j in range(n):
                # increment count for all 1s fresh orange
                if grid[i][j] == 1:
                    freshCount += 1
                # add all 2s rotten orange                    
                if grid[i][j] == 2:
                    q.append((i, j))
                    visitted.add((i, j)) # grid[i][j] = 2 set as rotten after visit

        while q and freshCount:
            size = len(q)
            level += 1
            for _ in range(size):
                i, j = q.popleft()
                for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visitted and grid[x][y] == 1:
                        # mat[x][y] = mat[i][j] + 1
                        q.append((x, y))
                        visitted.add((x, y)) # grid[i][j] = 1 to avoid using visited set
                        freshCount -= 1

        return level if freshCount == 0 else -1
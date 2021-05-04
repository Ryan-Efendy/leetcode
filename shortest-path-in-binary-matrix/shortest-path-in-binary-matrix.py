class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        -1,1      0,1     1,1
        
        -1,0      0,0     1,0
        
        -1,-1     0,-1    1,-1
        
        start: 0,0
        goal:   m-1, n-1
        '''
        # edge case if start (0,0) or end (m-1,n-1) is a 1
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1: return -1
        
        q = collections.deque()
        visited = set()
        level = 0

        # init start (0,0) to queue
        q.append((0, 0))
        visited.add((0, 0))

        # bfs
        while q:
            level += 1
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                # goal
                if i == m-1 and j == n-1:
                    return level
                for dx, dy in [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]:
                    x, y = i + dx, j + dy
                    # is not out of bound, is not visited and is a 0
                    if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited and grid[x][y] == 0:
                        q.append((x, y)) # 3. process its children
                        visited.add((x, y)) # add to visited
        # no path to goal
        return -1
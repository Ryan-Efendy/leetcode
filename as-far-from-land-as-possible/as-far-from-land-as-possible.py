class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/as-far-from-land-as-possible/discuss/360963/C%2B%2B-with-picture-DFS-and-BFS
        same as 01 Matrix and Walls and Gates
        0 represents water & 1 represents land
        
        [
            [\U0001f3dd,\U0001f30a,\U0001f3dd],
            [\U0001f30a,\U0001f30a,\U0001f30a],
            [\U0001f3dd,\U0001f30a,\U0001f3dd]
        ]
        '''
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visitted = set()
        level = 0

        # init - add all 1s (land) to queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visitted.add((i, j))
        
        if len(q) == m * n or len(q) == 0: return -1

        # bfs
        while q:
            size = len(q)
            level += 1
            for _ in range(size):
                i, j = q.popleft()
                for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visitted:
                        # mat[x][y] = mat[i][j] + 1
                        q.append((x, y))
                        visitted.add((x, y)) 
        return level-1
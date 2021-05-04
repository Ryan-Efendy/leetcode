class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        BFS enqueue all 0s, poll 0s check neighbor == INF then update it to curr+1
        """
        if not rooms or not len(rooms) or not len(rooms[0]): return
        m, n = len(rooms), len(rooms[0])
        INF = 2**31 - 1
        q = collections.deque()
        
        # enqueue all 0s
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    
        while q:
            i, j = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + dx, j + dy
                if x >= 0 and x < m and y >= 0 and y < n and rooms[x][y] == INF:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x, y))
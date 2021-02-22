class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not len(rooms) or not len(rooms[0]): return
        m, n = len(rooms), len(rooms[0])
        visitted = set()
        q = collections.deque()
        # init
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: # check if it's a gate
                    q.append((i, j))
                    visitted.add((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x >= 0 and x < m and y >= 0 and y < n and rooms[x][y] != -1 and (x, y) not in visitted:
                    rooms[x][y] = min(rooms[x][y], rooms[i][j] + 1)
                    q.append((x, y))
                    visitted.add((x, y))
                    
            
            
        
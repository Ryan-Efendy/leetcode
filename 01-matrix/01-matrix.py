class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        BFS - add all 0's to queue
        
        [    0 1 2
          0 [0,0,0],
          1 [0,1,0],   Q = [(0,0), (0,1), (0,2), (1,0), (1,2)]
          2 [1,1,1]
        ]
        
        '''
        if not mat or not len(mat): return mat
        m, n = len(mat), len(mat[0])
        q = collections.deque()
        visitted = set()

        # init - add all 0's to queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visitted.add((i, j))

        # bfs
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft() # 1. pull node
                for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]: # getting all the neighbors
                    x, y = i + dx, j + dy
                    # check if it's valid & hasn't been visitted yet (all 0's are visited so won't update 0's)
                    if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visitted:
                        mat[x][y] = mat[i][j] + 1 # 2. process node
                        q.append((x, y)) # 3. process its children
                        visitted.add((x, y)) # add to visited
        return mat
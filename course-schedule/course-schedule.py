class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        '''
        https://www.youtube.com/watch?v=L05HDfyDHjg
        indegree - # of nodes coming in
        outdegree  - # of nodes going out
        
        topological sort
        1. get mapping vertex:indegrees
        2. vertex w/ 0 indegree is the start
        3. process start & remove 1 indegree from neighbors, add any vertex w/ 0 indegree & repeat until queue is empty
            otherwise cycle exists
            
        kahn's algo
        1. node w/ indegree=0 is start
        2. reduce indegree of currNode neigh
        3. insert node w/ indegree=0
        4. if # remove connections == # nodes: no cycle else cycle exists
        
        if there's no node w/ indegree=0 there's a cycle
        '''
        # construct graph & calc inDegrees
        graph = defaultdict(set)
        inDegrees = {i:0 for i in range(n)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            inDegrees[edge[1]] += 1
        
        q = collections.deque()
        visited = set()
        
        # find nodes whose in degree == 0
        for index, in_degree in inDegrees.items():
            if in_degree == 0:
                q.append(index)
                
        # loop all nodes whose in degree == 0
        while q:
            index = q.popleft()
            visited.add(index)
            for g in graph[index]:
                inDegrees[g] -= 1
                if inDegrees[g] == 0:
                    q.append(g)
        return len(visited) == n # all courses will be visited
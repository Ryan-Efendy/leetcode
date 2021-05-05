class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Detect cycle in an undirected graph/return all the nodes that are not a part of the cycle
        
        graph = [[1,2],[2,3],[5],[0],[5],[]]    
        {
            0: [1,2],
            1: [2,3],
            2: [5],
            3: [0],
            4: [5],
            5: []
        }
        
        0->1->3->0 ❌ cycle
        
        0: 0->1->3->0
        1: 1->3->0->1
        3: 3->0->1->3
       
       https://www.youtube.com/watch?v=6ySoJbyBs4E
       
        0: non-visited
        1: safe (terminal)
        2: unsafe (cycle)
        
        graph (3) colors 
        visited[node] == 0: non-visited
        visited[node] == 1: inProgress
        node in cycle ==  : completed
        
        '''
        def dfs(node, path, visited, cycle):
            # if node is inProgress or cycle has already been detected
            if visited[node] == 1 or node in cycle:
                cycle |= set(path) # union
            elif visited[node] == 0:
                path.append(node)
                visited[node] = 1 # change to inProgress
                for child in graph[node]:
                    dfs(child, path, visited, cycle)
                visited[node] = 2 # update to complete
                path.pop() # backtrack?

        cycle, visited = set(), [0] * len(graph)
        for node in range(len(graph)):
            dfs(node, [], visited, cycle)
        # difference
        return sorted(set(range(len(graph))) - cycle)

    

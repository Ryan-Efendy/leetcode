class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        self.dfs(rooms, 0, visited)
        return 0 not in visited
    
    def dfs(self, graph, node, visited):
        if not visited[node]:
            visited[node] = 1
            for neighbour in graph[node]:
                self.dfs(graph, neighbour, visited)
                    
        
    
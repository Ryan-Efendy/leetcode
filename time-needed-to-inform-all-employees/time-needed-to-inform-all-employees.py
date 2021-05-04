class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, currTime):
            nonlocal res
            # optimization check if node doesn't have any edges/leaf
            if node not in graph:
                res = max(res, currTime)
            
            for employee in graph[node]:
                dfs(employee, currTime + informTime[node])
    
        # build graph
        graph = defaultdict(list)
        for employee, manager in enumerate(manager):
            graph[manager].append(employee)
            
        res = 0
        dfs(headID, 0)
        return res
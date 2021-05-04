class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Detect cycle in an undirected graph
        
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
        '''
        n = len(graph)
        color = [0] * n
        res = []
        
        def dfs(start, color):
            # if a node is marked as 2, it means you are currently checking out what you can reach starting from it.
            if color[start] == 2:
                # So if you reach a node marked as 2, that means there is a loop, because you went deeper into the loop but came out somewhere on a top level node
                return False                     
            # 1 means the node was marked completely visited, so you've checked out all its paths it could reach. The only way a node can be marked as 1 is if all 
            elif color[start] == 1:              
                # the following code completes without problems. That means no loop was detected in any of the paths starting from the "start" node.
                return True                         

            # You are exploring all paths from "start" node so mark it as being explored ("unsafe"). If you go deeper but came back out to here, then a loop must       
            color[start] = 2                                                                     
            # exist in the path you are trying to explore.     
            for end in graph[start]:
                # check path of all neighbors of the "start" node to see if a loop exists. If it does then this node leads to a loop so return False.
                if not dfs(end, color):
                    return False
            # You have finished exploring all possible nodes you can reach from "start" node and found no loops so all paths starting from this node is "safe"
            color[start] = 1                    
            return True

        for i in range(len(graph)):
            if dfs(i, color):
                res.append(i)

        return res

    

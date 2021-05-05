class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        https://leetcode.com/problems/find-eventual-safe-states/discuss/816985/Python-easy-solution..-Graph-coloring-(98.69)
        
        '''
        # 0 = not processed     1 = processing     2 = processed
        def cycle(ind):
            if color[ind] == 1:
                return True   # true means that there is a cycle
            if color[ind] == 2:
                return False   # no cycle is present
            
            color[ind] = 1
            
            for node in graph[ind]:
                if cycle(node):
                    return True            
            color[ind] = 2
            return False
  
        n = len(graph)
        color = [0]*n  
        
        for i in range(len(graph)):
            cycle(i)     
        
        return [i for i in range(n) if color[i] == 2]

    

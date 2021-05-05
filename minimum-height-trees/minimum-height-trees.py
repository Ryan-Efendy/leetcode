class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''                                         3
                                                    |
                                                    2
        topological sort + BFS                      |
        - keep removing the leaf nodes i.e.   3--2--1--2--3
             remove the 3...2..until you get        | 
                to the center                       2
                  until two or less                 |
                                                    3   
                                                    
        - remove leaf node => subtract indegree from the parent
        
        https://leetcode.com/problems/minimum-height-trees/discuss/923055/Python-O(n)-by-leave-node-removal-w-Visualization
        https://www.youtube.com/watch?v=OsvbLAaRmu8
        '''    
        if n == 1: return [0]
        
        # build adjacency matrix
        adj_matrix = defaultdict(set)
        for parent, child in edges:
            adj_matrix[parent].add(child)
            adj_matrix[child].add(parent)
            
        # get leaves node indegree is 1 vs. normal topological indegree=0
        leave_nodes_queue = [ node for node in adj_matrix if len(adj_matrix[node]) == 1 ]
        
        # keep doing leave nodes removal until total node count is smaller or equal to 2
        while n > 2:
            n -= len(leave_nodes_queue)
            leave_nodes_next_round = []
            # leave nodes removal
            for leaf in leave_nodes_queue:
                neighbor = adj_matrix[leaf].pop() # set > list O(1) add/remove
                adj_matrix[neighbor].remove(leaf)
                
                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append( neighbor )
                    
            leave_nodes_queue = leave_nodes_next_round
        
        # final leave nodes are root node of minimum height trees
        return leave_nodes_queue
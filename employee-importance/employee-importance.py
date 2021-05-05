"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        '''
        employees=[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], id=1
        
                        1|5          5+3+3=11
                       /   \ 
                      /     \
                    2|3     3|3   
                    
        employees=[[1, 5, [2]], [2, 3, []], [3, 3, []]], id=1
                        
                        1|5   3|3        5+3=8
                       /     
                     2|3 
        BFS/DFS
        
        '''
        idToEmployee = {employee.id: employee for employee in employees}
        
        def dfs(id: int) -> int:
            for subordinate in idToEmployee[id].subordinates:
                idToEmployee[id].importance += dfs(subordinate)
            return idToEmployee[id].importance
        
        return dfs(id)
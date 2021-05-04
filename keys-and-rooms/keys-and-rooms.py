class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        https://www.youtube.com/watch?v=DoHwPeLKQmw
        https://www.youtube.com/watch?v=8iUFLUIeK9k
        
                      0   1   2   3
        Ex 1 Input: [[1],[2],[3],[]] => room0 -> room1 -> room2 -> room3
             Output: true
             We start in room 0, and pick up key 1.
             We then go to room 1, and pick up key 2.
             We then go to room 2, and pick up key 3.
             We then go to room 3. Since we were able to go to every room, we return true. 
        
                                                             / \ <- cycle        /\ <- cycle  
        Ex 2 Input: [[1,3],[3,0,1],[2],[0]] => room0 <-> room1 /            room2 / 
                                                 ^         |
                                                 |         V
                                                 |-----> room3 
             Output: false   
             Explanation: We can't enter the room with number 2.
             
        from src vertex/node can we reach the rest of the nodes
        '''
        visited = set([0])
        
        def dfs(room):
            for neib in rooms[room]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib)
                    
        dfs(0)
        return len(visited) == len(rooms)    
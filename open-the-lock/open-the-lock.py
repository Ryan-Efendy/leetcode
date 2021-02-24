class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        lock = "0000"
        q = collections.deque()
        seen = set()
        deadends = set(deadends)
        # edge case if "0000" is in deadends
        if lock in deadends: return -1
        q.append((lock, 0))
        seen.add(lock)
        
        # bfs
        while q:
            lock, turn = q.popleft()
            if lock == target: return turn
            if lock in deadends: continue
            
            for neighbor in self.get_neighbors(lock):
                if neighbor not in deadends and neighbor not in seen:
                    q.append((neighbor, turn+1))
                    seen.add(neighbor)
        return -1
        
    def get_neighbors(self, lock):
        #            0     1    2     3      4     5    6     7
        # 0000 -> [1000, 9000, 0100, 0900, 0010, 0090, 0001, 0009]
        locks = []
        for i in range(len(lock)):
            for delta in (1, -1):
                new_lock_i = (int(lock[i]) + delta) % 10 # -1 % 10 = 9
                new_lock = lock[:i] + str(new_lock_i) + lock[i+1:]
                locks.append(new_lock)
        return locks
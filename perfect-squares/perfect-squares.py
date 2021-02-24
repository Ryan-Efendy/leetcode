class Solution:
    def numSquares(self, n: int) -> int:
        q = collections.deque()
        seen = set()
        sqrRoot = math.floor(math.sqrt(n)) #floor(sqrt(12)) = 3
        perfectSquares = [i*i for i in range(1, sqrRoot+1)] #[1, 4, 9]
        q.append((n, 1))
        
        # bfs
        while q:
            n, level = q.popleft()
            
            for perfectSquare in perfectSquares:
                remainder = n - perfectSquare
                if remainder == 0: return level
                if remainder > 0 and remainder not in seen:
                    seen.add(remainder)
                    q.append((remainder, level+1))
                elif remainder < 0:
                    break
        return 0
        
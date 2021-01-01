class Solution:
    '''
    a + b + c + d = 0 => a + b = - c - d
    
    '''
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        n = len(A)
        map = defaultdict(int)
        
        for a in A:
            for b in B:
                map[a+b] += 1
        
        for c in C:
            for d in D:
                val = -(c+d)
                if val in map:
                    res += map[val]
        
        return res
        

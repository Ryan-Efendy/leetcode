class Solution:
    '''
    num = 25
    
    l = 4
    r = 5
    m = 5
    '''
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num//2
        while l < r:
            m = l + (r-l)//2
            if m**2 < num:
                l = m + 1
            else:
                r = m
        return l*l == num
        

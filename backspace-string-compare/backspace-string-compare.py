class Solution:
    '''
    S = "ab#c"
            ij
    T = "ad#c"
            ij
    
    S = "ab##"
         i
    T = "c#d#"
         j
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1, s2 = [], []
        for s in S:
            if s != '#':
                s1.append(s)
            else:
                if len(s1): s1.pop()
                
        for t in T:
            if t != '#':
                s2.append(t)
            else:
                if len(s2): s2.pop()
                
        return s1 == s2
        

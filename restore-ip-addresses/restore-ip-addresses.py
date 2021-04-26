class Solution:        
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        Input: s = "101023"
        Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        
        '''
        self.res = []
        self.backtrack(s, [], 0)
        return self.res
    
    def backtrack(self, s, current, start):
        # goal, check if curr is 4 X.X.X.X and if all of s is used up i.e. s="101023"
        if len(current) == 4 and start == len(s):
            self.res.append(".".join(current))
            return
        if len(current) > 4:
            return
        for i in range(start, min(start+3, len(s))):
            """
            Check if the current segment is valid :
            1. less or equal to 255      
            2. the first character could be '0' 
               only if the segment is equal to '0'
            """
            if s[start] == '0' and i > start: # constraint
                continue
            if int(s[start:i+1]) <= 255: # 1. Choices
                current.append(s[start:i+1]) # choose
                self.backtrack(s, current, i + 1) # explore
                current.pop() # unchoose
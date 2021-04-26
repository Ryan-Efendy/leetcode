class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Input: s = "aab"
                        "aab"
                     /    |    \
                  a✅    aa✅    aab❌ 
                /  |      |
               a✅  ab❌   b✅
               |
               b✅
            
        Output: [["a","a","b"],["aa","b"]]
        '''    
        res = []

        def backtrack(path, i):
            if i >= len(s): # goal
                res.append(path[:])
                return
            for j in range(i, len(s)): # choices
                if not self.isPalindrome(s, i, j): # constraint
                    continue
                path.append(s[i:j+1]) # choose
                backtrack(path, j+1) # explore
                path.pop()           # unchoose

        backtrack([], 0)
        return res


    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
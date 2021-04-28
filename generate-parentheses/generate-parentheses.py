class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        requirements for valid expressions
        1. should not start with ')'
        2. size of '(' <= n
        3. size of '(' >= ')'
        '''
        def backtrack(opened, closed, s):
            if opened == n and closed == n: # goal
                res.append(s)
                return
            # 2
            if opened < n: # constraint
                backtrack(opened+1, closed, s+'(') # choice 1
            # 3
            if opened > closed: # constraint
                backtrack(opened, closed+1, s+')') # choice 1

        res = []
        backtrack(0, 0, '')
        return res
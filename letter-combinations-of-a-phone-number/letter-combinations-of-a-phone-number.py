class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'1': '', '2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        length = len(digits)
        res = []
        
        if (length == 0):
            return res
        
        def backtrack(idx, candidate, digits, mapping, res):
            if (idx == len(digits)):
                res.append(candidate)
                return
                
            for next_char in mapping[digits[idx]]:
                candidate += next_char
                # print(next_char)
                backtrack(idx+1, candidate, digits, mapping, res)
                candidate = candidate[0:-1]
        
        backtrack(0, "", digits, mapping, res)
        
        return res
        
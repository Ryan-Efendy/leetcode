class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        digits = "23"
                            "23"
                           / |  \ 
                          /  |   \
                        a    b     c
                     / |\   /|\    /|\
                    /  | \ / | \  / | \ 
                 ad ae af bd be bf cd ce cf       
        Time Complexity: O(n^3), Space complexity: O(n)
        '''
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(idx, path):
            if len(path) == len(digits): # goal
                res.append("".join(path))
                return
            
            for letter in letters[digits[idx]]: # Choices
                path.append(letter) # choose
                backtrack(idx + 1, path) # explore
                path.pop() # unchoose

        res = []
        if len(digits) == 0: 
            return res
        backtrack(0, [])
        return res
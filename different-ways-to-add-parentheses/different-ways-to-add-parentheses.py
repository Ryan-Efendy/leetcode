class Solution:
    def diffWaysToCompute(self, expression: str, memo: dict={}) -> List[int]:
        '''
        top-down
                          \U0001f447   \U0001f447  \U0001f447
                        "2 * 3 - 4 * 5"
                         /     |      \
                     6-4*5   2*-1*5    2*3-20
                   /   \      /  \       /  \
                 2*5  6-20 -2*5  2*-5  6-20  2*-17
                  |     |    |     |     |     |
                 10    -14  -10   -10   -14   -34
                 
        bottom-up is better, prune dups        
        '''
        if expression.isdigit():
            return [int(expression)]
        if expression in memo:
            return memo[expression] 
        res = []
        for i in range(len(expression)):
            if expression[i] in "-+*":
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, expression[i]))
        memo[expression] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
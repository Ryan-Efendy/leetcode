class Solution:
    def diffWaysToCompute(self, expression: str, memo: dict={}) -> List[int]:
        '''
        https://www.youtube.com/watch?v=binXv9-uT3A
        top-down < bottom-up is better, prune dups   
        
                          \U0001f447   \U0001f447  \U0001f447
                        "2 * 3 - 4 * 5"
                         /     |      \
                 (2*3)-4*5  2*(3-4)*5  2*4-(4*5)  
                     6-4*5   2*-1*5    2*3-20
                   /   \      /  \       /  \
            (6-4)*5  6-(4*5) 
                 2*5  6-20 -2*5  2*-5  6-20  2*-17
                  |     |    |     |     |     |
                 10    -14  -10   -10   -14   -34
                 
                        f(2-1-1)
                          /     \
                         /       \                           
                  f(2)-f(1-1)  f(2-1)-f(1)
                   2 - 0 = 2    1 - 1 = 0
                
                            f(2*3-4*5)
                            /    |      \
                          /      |        \
                        /        |          \
            f(2)*f(3-4*5)   f(2*3)-f(4*5)  f(2*3-4)*f(5)
                  /  \          |     |        |       
                /      \        |     |   f(2)*f(3-4)
        f(3)-f(4*5) f(3-4)*f(5) |     |           |
                /     \         |  f(4)*f(5)     / 
               /       \   f(2)*f(3)            /
         f(4)*f(5)  f(3)-f(4)             f(3)-f(4)
         
         
        '''
        # check if all chars are digits
        if expression.isdigit():
            return [int(expression)]
        if expression in memo:
            return memo[expression] 
        res = []

        for i in range(len(expression)):
            if expression[i] in "-+*":
                # break expression into 2 i.e. f(2*3-4) -> f(2) * f(3-4)
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i+1:])
                # base case? 2 operators & 1 operand i.e. 2*3
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
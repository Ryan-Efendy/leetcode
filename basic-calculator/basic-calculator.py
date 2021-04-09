class Solution:
    def calculate(self, s: str) -> int:
        '''
        12-(2-3)
              i
        res=-1
        sign=-1
        1+12 -> 13

        [12, -1]

        1.Using res to keep track of the current calculated result.
        2.Using op to keep track of the operator.
        3.Using num to keep track of the current number used to update res.
        4.If needed, using prev to keep track of previous number added to the res.
        5.Go through each char in the string
            5.1.if meet (, push res, op, prev, to stack.
            5.2 if meet ), update res, pop whatever is in the stack
            5.3 if meet operator, update res
            5.4 if meet digit, update num
            Small trick: add an extra + to the end of string to make sure the entire string is evaluated.
        '''
        def update(a, b, op):
            return a + b if op == '+' else a - b

        s += '+' # hack
        stack = []
        op = '+'
        res = num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ['+', '-']:
                res = update(res, num, op)
                num = 0
                op = char
            elif char == '(':
                stack.append((res, op))
                op = '+'
                res = num = 0
            elif char == ')':
                num = update(res, num, op)
                res, op = stack.pop()
        return int(res)
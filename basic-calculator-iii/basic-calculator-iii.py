class Solution:
    def calculate(self, s: str) -> int:
        '''
        https://leetcode.com/problems/basic-calculator-iii/discuss/276478/Python-one-simple-template-solving-basic-calculator-I-and-III

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
        def update(a, b, prev, op):
            if op == '-':
                b *= -1
            if op == '*':
                a -= prev
                b *= prev
            if op == '/':
                a -= prev
                sign = 1 if prev > 0 else -1
                b = int(abs(prev) / b) * sign
            return a + b, b
        
        s += '+'
        stack = []
        op = "+"
        res = num = prev = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ["+", "-", "*", "/"]:
                res, prev = update(res, num, prev, op)
                num = 0
                op = char
            elif char == '(':
                stack.append((res, prev, op))
                op = '+'
                res = num = prev = 0
            elif char == ')':
                num, prev = update(res, num, prev, op)
                res, prev, op = stack.pop()
        return int(res)
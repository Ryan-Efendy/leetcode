class Solution:
    def calculate(self, s: str) -> int:
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
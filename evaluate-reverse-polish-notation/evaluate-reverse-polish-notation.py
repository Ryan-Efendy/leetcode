class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x/y)
        }
        for token in tokens:
            if token in operators:
                operand1, operand2 = s.pop(), s.pop()
                res = operators[token](int(operand2), int(operand1))
                s.append(res)
            else:
                s.append(token)
        return s.pop()
                
            
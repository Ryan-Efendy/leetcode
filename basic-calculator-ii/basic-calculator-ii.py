class Solution:
    def calculate(self, s: str) -> int:
        '''
        1. if the curr op is +|- then the exp is eval based on the precedence of next op.
        2. if the curr op is *|/ then the exp is eval irrespective of next op
        '''
        if not s: return 0

        stack, curr_num, operator = [], 0, '+'
        operators = {'+', '-', '*', '/'}
        operands = set(str(i) for i in range(10))

        for i in range(len(s)):
            char = s[i]
            # if char is operand (0-9) add it to curr_num
            if char in operands:
                curr_num = curr_num * 10 + int(char)

            if char in operators or i == len(s)-1:
                # 1. +/- have lower precedent, eval later based on next operation
                # push to curr_num stack to be eval later based on next op
                if operator == '+':
                    stack.append(curr_num)

                elif operator == '-':
                    stack.append(-curr_num)

                # 2. */- highest precent eval right away
                # pop top of stack and eval right away
                elif operator == '*':
                    stack[-1] *= curr_num

                elif operator == '/':
                    stack[-1] = int(stack[-1] / curr_num)

                curr_num = 0
                operator = char

        return sum(stack)
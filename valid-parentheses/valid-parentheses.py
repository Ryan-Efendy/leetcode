class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ('(', '[', '{'):
                stack.append(bracket)
            else:
                if not stack or not len(stack):
                    return False
                open_bracket = stack.pop() 
                if bracket == ')' and not open_bracket == '(':
                    return False
                elif bracket == ']' and not open_bracket == '[':
                    return False
                elif bracket == '}' and not open_bracket == '{':
                    return False
        return not len(stack)
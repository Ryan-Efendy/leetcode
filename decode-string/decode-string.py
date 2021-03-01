class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c.isalpha():
                newStr = stack[-1][0] + c
                stack[-1] = [newStr, stack[-1][1]]
            elif c == "[":
                stack.append(["", num])
                num = ""
            elif c == "]":
                oldStr, k = stack.pop()
                newStr = oldStr * int(k)
                stack[-1] = [stack[-1][0] + newStr, stack[-1][1]]
        return stack.pop()[0]
            
            
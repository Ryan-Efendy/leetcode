class Solution:
    def simplifyPath(self, absolute_path: str) -> str:
        stack = []
        paths = absolute_path.split('/')
        for path in paths:
            if path == '.' or path == '':
                continue
            elif path == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return '/' + "/".join(stack)
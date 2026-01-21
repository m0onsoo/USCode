class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        delimiter = '/'
        path_list = path.split(delimiter)

        stack = []
        for p in path_list:
            if p == '' or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)

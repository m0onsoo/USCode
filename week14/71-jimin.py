# https://leetcode.com/problems/simplify-path/
# 71-simplify-path


class Solution:
    def simplifyPath(self, path: str) -> str:
        # split path with /
        # put elems in stack
        # if .., pop one
        # if ., stay
        # else : put in stack
        # recursively concat path

        path_elems = path.split("/")
        path_stack = []

        for elem in path_elems:
            if elem == "..":
                if path_stack:
                    path_stack.pop()
                else:
                    continue
            elif elem == "." or elem == "":
                continue
            else:
                path_stack.append(elem)

        # -> 이 부분은 "/".join(stack)으로 쉽게 할 수 있었다...
        simplified_canonical_path = ""
        while path_stack:
            if not simplified_canonical_path:
                simplified_canonical_path = path_stack.pop()
            else:
                simplified_canonical_path = (
                    path_stack.pop() + "/" + simplified_canonical_path
                )

        return "/" + simplified_canonical_path

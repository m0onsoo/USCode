# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# 150-evaluate-reverse-polish-notation

import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            stack.append(token)

        def calc(s):
            if not s:
                return
            cur = s.pop()
            if cur in operators:
                right = calc(s)
                left = calc(s)
                if cur == "+":
                    return int(left) + int(right)
                elif cur == "-":
                    return int(left) - int(right)
                elif cur == "*":
                    return int(left) * int(right)
                elif cur == "/":
                    return int(int(left) / int(right))
            else:
                return int(cur)

        return calc(stack)

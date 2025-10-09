from typing import List

# 0ms, 19.2MB
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '/', '*']
        stack = []

        for i, token in enumerate(tokens):
            if token in ops:
                # calculate according to the operator
                n2, n1 = stack.pop(), stack.pop()
                result = self.calculate(n1, n2, token)

                # insert calculated result into stack
                stack.append(result)
            else:
                # if token is number, insert into stack
                stack.append(token)
        
        return int(stack[0])
    
    def calculate(self, n1: str, n2: str, op: str) -> str:
        n1, n2 = int(n1), int(n2)
        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        else:
            result = int(n1 / n2)
        
        return str(result)
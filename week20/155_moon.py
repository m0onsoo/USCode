import numpy as np

class MinStack:

    def __init__(self):
        self.stack = []
        # self.min = np.inf
        # self.sec_min = np.inf
        self.min = (-1, np.inf)
        self.idx = 0
        # stack = [ (idx, num, (min_idx, min_num))]

    def push(self, val: int) -> None:
        self.stack.append((self.idx, val, self.min))
        self.idx += 1
        if val < self.min[1]:
            self.min = (self.idx, val)

    def pop(self) -> None:
        if not self.stack:
            return False

        if self.stack[-1][1] == self.min[1]:
            self.min = self.stack[-1][2]
        del self.stack[-1]
        self.idx -= 1


    def top(self) -> int:
        if not self.stack:
            return False
        
        return self.stack[-1][1]
        

    def getMin(self) -> int:
        if not self.stack:
            return False
        
        return self.min[1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
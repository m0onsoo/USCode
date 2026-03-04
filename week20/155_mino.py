class MinStack:

    def __init__(self):
        self.elems = []
        # self.minValue = float('inf')
    def push(self, val: int) -> None:
        minValue = min(self.elems[-1][1], val) if self.elems else val
        self.elems.append([val, minValue])
        
    def pop(self) -> None:
        self.elems.pop()
        # self.minValue = float('inf')
        # self.minValue = self.elems[-1][1]

    def top(self) -> int:
        return self.elems[-1][0]
        
    def getMin(self) -> int:
        return self.elems[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
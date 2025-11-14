class MinStack:
# [push: 2, 3, pop, -2, top, getMin, 5] -> stack=[2, -2, 5, -10], minHeap=[2, -2, -10]
    def __init__(self):
        self.stack = []
        self.minHeap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minHeap or val <= self.minHeap[-1]:
            self.minHeap.append(val)
        
    def pop(self) -> None:
        popVal = self.stack.pop()
        if popVal == self.minHeap[-1]:
            self.minHeap.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHeap[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
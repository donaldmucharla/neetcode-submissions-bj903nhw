class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(min(val, self.minStack[-1]))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
        
    def top(self) -> int:
         if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

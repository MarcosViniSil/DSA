#Link to problem: https://leetcode.com/problems/min-stack/description/
#Time complexity: O(1)
#Space complexity: O(n)

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        local_min = val
        if self.stack:
            local_min = min(self.stack[-1][1],val)
        self.stack.append((val,local_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]
    

minStack = MinStack();
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())   # return 0
print(minStack.getMin()) # return -2

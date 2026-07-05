class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in operations:
            if c == "+":
                x = stack[-1]
                y = stack[-2]
                stack.append(x+y)
            elif c == "C":
                stack.pop()
            elif c == "D":
                x = stack[-1]
                stack.append(2*x)
            else:
                stack.append(int(c))
        return sum(stack)

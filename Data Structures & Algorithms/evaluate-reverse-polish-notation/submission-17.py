class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif t == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif t == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            elif t == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            else:
                stack.append(int(t))
        return stack[0]
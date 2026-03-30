class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # Pop until stack is increasing
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))

        # Process remaining stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
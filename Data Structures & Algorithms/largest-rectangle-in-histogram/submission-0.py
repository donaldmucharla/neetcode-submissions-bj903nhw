class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            # If current height is less than the height at the top of stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area: height * (current_index - original_start_index)
                maxArea = max(maxArea, height * (i - index))
                # The start index for the current shorter bar moves back
                start = index
            stack.append((start, h))

        # After the loop, some bars might still be in the stack
        # They extend all the way to the end of the histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea
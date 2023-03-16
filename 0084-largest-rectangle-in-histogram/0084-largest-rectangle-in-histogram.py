class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_square = 0
        stack = []
        for i, height in enumerate(heights):
            tmp = i
            while stack and stack[-1][1] > height:
                p_idx, p_height = stack.pop()
                p_width = i - p_idx
                max_square = max(max_square, p_width * p_height)
                tmp = p_idx
            stack.append([tmp, height])
            
        while stack:
            idx, height = stack.pop()
            width = len(heights) - idx
            max_square = max(max_square, width * height)
            
        return max_square
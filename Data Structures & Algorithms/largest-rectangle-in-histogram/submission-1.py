class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                area = max(area,(i - ind)*height)
                start = ind
            
            stack.append([start,h])
        
        for i, h in stack:
            a = h*(len(heights)-i)
            area = max(a,area)
        
        return area
            




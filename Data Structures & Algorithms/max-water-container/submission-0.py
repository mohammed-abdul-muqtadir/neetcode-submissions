class Solution:
    def maxArea(self, heights: List[int]) -> int:

        water = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            
            
            held = (j-i) * min(heights[i],heights[j])

            water = max(held,water)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return water










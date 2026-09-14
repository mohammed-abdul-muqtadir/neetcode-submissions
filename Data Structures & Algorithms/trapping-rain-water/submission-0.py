class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height)-1
        lh = 0
        rh = 0
        while l < r:
            if height[l] > lh:
                lh = height[l]
            if height[r] > rh:
                rh = height[r]

            cr = min(lh,rh)
            
            if height[l] > height[r]:
                r -= 1
                if cr > height[r]:
                    ans += cr - height[r]
            else:
                l += 1
                if cr > height[l]:
                    ans += cr - height[l]

        return ans
            


            

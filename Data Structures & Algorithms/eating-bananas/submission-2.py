class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        bot = 1
        ans = float("inf")
        top = max(piles)
        if n == h:
            return top

        def check(p,h,m):

            time = sum(-(-pile//m) for pile in p)
            return h >= time

        while bot <= top:
            
            m = (top+bot)//2
            if check(piles,h,m):
                top = m-1
                ans = min(ans,m)
            else:
                bot = m + 1
        
        return ans

        
        
        
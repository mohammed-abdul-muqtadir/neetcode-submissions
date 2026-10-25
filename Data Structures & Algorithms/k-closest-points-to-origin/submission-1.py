class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        from math import sqrt

        h = []
        ans = []

        for i,j in points:
            x = sqrt(((i)**2)+((j)**2))
            heapq.heappush(h,[x,i,j])
        
        for i in range(k):
            d,x,y = heapq.heappop(h)

            ans.append([x,y])
        
        return ans
        

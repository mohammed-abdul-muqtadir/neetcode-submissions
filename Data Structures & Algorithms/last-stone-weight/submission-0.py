class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            c = -abs(a - b)
            heapq.heappush(stones,c)
        
        return -stones[0] if stones else 0



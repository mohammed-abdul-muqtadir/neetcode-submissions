class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        slow = 0
        for fast in range(1,len(prices)):
            if prices[fast] < prices[slow]:
                slow = fast
            ans = max(ans,prices[fast]-prices[slow])

        return ans
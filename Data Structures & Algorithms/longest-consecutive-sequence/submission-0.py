class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numbers = set(nums)
        for n in nums:
            if n - 1 not in numbers:
                steak = 1
                curr = n
                while curr + 1 in numbers:
                    steak += 1
                    curr += 1
                ans = max(ans,steak)
            
        return ans

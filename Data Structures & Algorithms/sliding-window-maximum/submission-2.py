class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        a = deque()
        ans = []
        for i in range(len(nums)):

            while a and nums[a[-1]] < nums[i]:
                a.pop()
            
            a.append(i)

            if a[0] < i-k+1:
                a.popleft()
            
            if i >= k-1:
                ans.append(nums[a[0]])
            
        return ans
            


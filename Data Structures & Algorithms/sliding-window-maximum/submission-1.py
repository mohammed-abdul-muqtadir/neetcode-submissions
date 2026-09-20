class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n*k == 0:
            return []
        if k == 1:
            return nums
        
        leftmax = [0]*n
        rightmax = [0]*n

        leftmax[0] = nums[0]
        rightmax[-1] = nums[-1]

        for r in range(1, n):
            
            if r % k == 0:
                leftmax[r] = nums[r]
            else:
                leftmax[r] = max(nums[r],leftmax[r-1])
            
            l = n - r -1
            if (l + 1) % k == 0:
                rightmax[l] = nums[l]
            else:
                rightmax[l] = max(rightmax[l+1],nums[l])
            
        output = []

        for i in range(n-k+1):
            j = i + k - 1
            output.append(max(leftmax[j],rightmax[i]))

        return output


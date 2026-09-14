class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if nums == []:
            return []

        nums.sort()
        ans = []

        for j in range(len(nums)):

            if j > 0 and nums[j] == nums[j-1]:
                continue
            
            i = j+1
            k = len(nums)-1

            while i < k:

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i],nums[j],nums[k]])

                    while i < k and nums[i] == nums[i + 1]:
                        i += 1
                    while i < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    i += 1
                    k -= 1

                
                elif total > 0:
                    k -= 1
                else:
                    i += 1
        return ans







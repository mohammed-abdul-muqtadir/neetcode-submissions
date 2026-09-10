class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        mul = 1
        for i in nums:
            if i == 0:
                zero += 1
                continue
            mul *= i

        if zero > 1:
            return [0 for i in range(len(nums))]
        
        if zero == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = mul
                else:
                    nums[i] = 0
            return nums

        
        for i in range(len(nums)):
            nums[i] = int(mul/nums[i])
        
        return nums
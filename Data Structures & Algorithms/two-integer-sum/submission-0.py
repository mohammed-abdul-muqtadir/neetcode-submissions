class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            rev = target - nums[i]
            if rev in seen:
                return [seen[rev],i]
            else:
                seen[nums[i]] = i
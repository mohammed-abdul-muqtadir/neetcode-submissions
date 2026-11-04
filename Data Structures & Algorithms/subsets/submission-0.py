class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            ans += [a + [i] for a in ans]

        return ans
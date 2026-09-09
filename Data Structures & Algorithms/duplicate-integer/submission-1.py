class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out = False
        hashmap = {}
        for i in nums:
           hashmap[i] = 1 + hashmap.get(i,0)
        
        for i,j in hashmap.items():
            if j >= 2:
                out = True
        return out
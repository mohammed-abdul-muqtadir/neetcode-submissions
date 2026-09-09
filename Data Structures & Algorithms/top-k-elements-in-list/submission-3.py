class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        arr = [[] for _ in range(len(nums)+1)]
        for j in count.keys():
            arr[count[j]].append(j)

        
        ans = []
        for i in range(len(arr)-1,0,-1):
            if arr[i]:
                for i in arr[i]:
                    ans.append(i)
                    if len(ans) == k:
                        return ans
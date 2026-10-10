class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)
        m = -1

        for i in range(len(arr)-1,-1,-1):
            ans[i] = m
            m = max(arr[i],m)
        
        return ans



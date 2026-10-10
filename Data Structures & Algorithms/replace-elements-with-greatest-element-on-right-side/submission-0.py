class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(arr)

        for i in range(len(arr)-1,-1,-1):

            if stack:
                ans[i] = stack[-1]
            if stack:
                if arr[i] > stack[-1]:
                    stack.append(arr[i])
            else:
                stack.append(arr[i])
        
        return ans



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        sta = []

        for i,t in enumerate(temperatures):
            while sta and t > sta[-1][0]:
                val, ind = sta.pop()
                ans[ind] = i - ind
            sta.append([t,i])
        
        return ans

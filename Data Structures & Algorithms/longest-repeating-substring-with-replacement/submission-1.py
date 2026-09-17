class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        dic = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r],0)
            maxf = max(maxf,dic[s[r]])

            while (r-l+1) - maxf > k:
                dic[s[l]] -= 1
                l += 1
            
            ans = max(ans,r-l+1)
        return ans

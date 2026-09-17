class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        has = set()
        ans = 0
        i = 0
        j = 0
        count = 0
        while j < len(s):
            while has and s[j] in has:
                has.remove(s[i])
                i += 1
                count -= 1
            
            has.add(s[j])
            j += 1
            count += 1
            ans = max(count,ans)
        
        return ans
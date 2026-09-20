class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""

        dic = {}
        window = {}
            
        for i in t:
            dic[i] = 1 + dic.get(i,0)

        have = 0
        need = len(dic)
        res = [-1,-1]
        reslen = float("inf")
        l = 0
        for r in range(len(s)):

            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in dic and window[s[r]] == dic[s[r]]:
                have += 1

            while have == need:

                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in dic and window[s[l]] < dic[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""

        





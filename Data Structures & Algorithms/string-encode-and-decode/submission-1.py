class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            length = len(i)
            ans += str(length) + "#" + i
        
        return ans


    def decode(self, s: str) -> List[str]:
        lis = []
        c = 0
        while c < len(s):
            j = s.find("#",c)
            l = int(s[c:j])

            word = s[j+1:j+1+l]
            lis.append(word)

            c = j + l + 1
        
        return lis
        
            

            

            
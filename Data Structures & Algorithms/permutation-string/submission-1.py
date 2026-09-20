class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s1 = "".join(s1)
        x = len(s1)
        print(s1)
        for i in range(len(s2)-len(s1)+1):
            a = "".join(sorted(s2[i:i + x]))
            print(a)
            if a == s1:
                return True
            
        return False

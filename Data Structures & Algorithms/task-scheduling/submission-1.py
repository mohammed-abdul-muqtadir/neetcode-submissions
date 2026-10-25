class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        c = [0]*26

        for i in tasks:
            c[ord(i)-ord('A')] += 1
        
        maxf = max(c)
        mc = 0
        for i in c:
            if i == maxf:
                mc += 1
        
        time = (maxf-1) * (n+1) + mc

        return max(time,len(tasks))
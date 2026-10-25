class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt

        dic = []
        a = 0
        for i in points:
            x = sqrt(((i[0])**2)+((i[1])**2))
            dic.append([x,i])
        dic.sort()
        ans = []
        for i in range(k):
            ans.append(dic[i][1])
        return ans

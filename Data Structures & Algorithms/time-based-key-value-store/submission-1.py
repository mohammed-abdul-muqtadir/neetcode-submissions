class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        val = self.dic.get(key,[])
        l = 0
        r = len(val) - 1
        while l <= r:
            m = l + (r-l)//2
            if val[m][1] <= timestamp:
                ans = val[m][0]
                l = m+1
            else:
                r = m-1
        return ans

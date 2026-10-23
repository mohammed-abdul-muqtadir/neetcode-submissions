class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lis = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.lis):
            if self.lis[i] > val:
                break
            i += 1
        
        self.lis.insert(i,val)
        return self.lis[-self.k]

        

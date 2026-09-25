class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = sorted(nums1+nums2)
        print(num3)
        k = len(num3)
        if len(num3)%2 == 0:
            return (num3[k//2]+num3[(k//2)-1])/2
        else:
            return num3[k//2]
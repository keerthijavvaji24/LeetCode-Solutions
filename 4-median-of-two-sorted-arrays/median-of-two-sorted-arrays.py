class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        m=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[m]
        else:return (nums1[m-1]+nums1[m])/2

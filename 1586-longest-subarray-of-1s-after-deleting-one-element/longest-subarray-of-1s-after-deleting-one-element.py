class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ml=0
        s=0
        z=-1
        for i in range(len(nums)):
            if nums[i]==0:
                s=z+1
                z=i
            ml=max(ml,i-s)
        return ml
        
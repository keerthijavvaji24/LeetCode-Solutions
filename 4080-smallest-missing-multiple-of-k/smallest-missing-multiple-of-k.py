class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        q=max(nums)
        for i in range(1,q+1):
            if i*k not in nums:
                return i*k
        else:return q+1


        
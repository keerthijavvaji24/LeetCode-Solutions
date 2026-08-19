class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        i=0
        while i<len(nums)-1:
            a=nums[i]
            b=nums[i+1]
            l.extend([b,a])
            i=i+2
        print(l)
        return l

        
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s=set(nums)
        print(s)
        for i in s:
            c=nums.count(i)
            if c%2!=0:return False
        else:
            return True